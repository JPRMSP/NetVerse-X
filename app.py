import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="NetVerse-X",
    page_icon="📡",
    layout="wide"
)

st.title("📡 NetVerse-X")
st.subheader("Interactive Next Generation Wireless Network Simulator")

# ==========================
# TABS
# ==========================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "GPRS/PDP",
    "IMS & SIP",
    "Mobility",
    "Security",
    "QoS",
    "Protocol Analyzer"
])

# =====================================================
# UNIT I : GPRS / PDP CONTEXT
# =====================================================
with tab1:

    st.header("GPRS Attach & PDP Context Activation")

    if st.button("Start GPRS Attach Procedure"):

        progress = st.progress(0)

        steps = [
            "Mobile Station -> BTS",
            "BTS -> SGSN",
            "Authentication Successful",
            "SGSN -> GGSN",
            "PDP Context Created",
            "Internet Access Granted"
        ]

        for i, step in enumerate(steps):
            progress.progress((i + 1) / len(steps))
            st.success(step)
            time.sleep(0.5)

        st.balloons()

    st.divider()

    st.subheader("PDP Context Details")

    pdp_ip = f"10.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

    st.json({
        "PDP_Context_ID": random.randint(1000, 9999),
        "IP_Address": pdp_ip,
        "APN": "internet.operator.com",
        "QoS_Class": random.choice([
            "Conversational",
            "Streaming",
            "Interactive",
            "Background"
        ])
    })

# =====================================================
# UNIT II : IMS / SIP
# =====================================================
with tab2:

    st.header("IMS Registration Simulator")

    if st.button("Register with IMS"):

        messages = [
            "REGISTER",
            "401 Unauthorized",
            "REGISTER (with credentials)",
            "200 OK"
        ]

        log_box = st.empty()

        for msg in messages:
            log_box.info(msg)
            time.sleep(1)

        st.success("IMS Registration Completed")

    st.divider()

    st.subheader("SIP Call Flow")

    if st.button("Simulate SIP Call"):

        sip_flow = [
            "INVITE",
            "100 TRYING",
            "180 RINGING",
            "200 OK",
            "ACK"
        ]

        for msg in sip_flow:
            st.write("📨", msg)
            time.sleep(0.5)

        st.success("Voice Session Established")

# =====================================================
# UNIT III : MOBILITY MANAGEMENT
# =====================================================
with tab3:

    st.header("Mobility & Handoff Simulator")

    position = st.slider(
        "Move Subscriber",
        0,
        100,
        10
    )

    if position <= 33:
        current_cell = "CELL-A"

    elif position <= 66:
        current_cell = "CELL-B"

    else:
        current_cell = "CELL-C"

    st.metric(
        "Connected Cell",
        current_cell
    )

    if position > 33:
        st.warning(
            "Handoff Detected - User moved to new coverage area"
        )

    st.metric(
        "Packet Delay",
        f"{random.randint(10,80)} ms"
    )

    st.metric(
        "Packet Loss",
        f"{random.randint(0,5)} %"
    )

    st.metric(
        "Serving SGSN",
        random.choice(["SGSN-1", "SGSN-2", "SGSN-3"])
    )

# =====================================================
# UNIT IV : SECURITY
# =====================================================
with tab4:

    st.header("Wireless Security Simulator")

    attack = st.selectbox(
        "Choose Attack",
        [
            "Man-In-The-Middle",
            "Replay Attack",
            "IP Spoofing",
            "Denial of Service"
        ]
    )

    if st.button("Launch Simulation"):

        st.error(f"{attack} detected")

        time.sleep(1)

        st.write("Applying Security Mechanisms")

        security_used = random.choice(
            [
                "IPSec Tunnel",
                "AAA Authentication",
                "AES Encryption",
                "Mutual Authentication"
            ]
        )

        st.info(f"Protection Activated : {security_used}")

        time.sleep(1)

        st.success("Threat Successfully Mitigated")

# =====================================================
# UNIT V : QoS
# =====================================================
with tab5:

    st.header("QoS Profile Manager")

    service = st.selectbox(
        "Traffic Type",
        [
            "Voice Call",
            "Video Streaming",
            "Online Gaming",
            "Email"
        ]
    )

    qos = {
        "Voice Call": [50, 5, "HIGH"],
        "Video Streaming": [100, 10, "MEDIUM"],
        "Online Gaming": [30, 3, "CRITICAL"],
        "Email": [300, 30, "LOW"]
    }

    delay, jitter, priority = qos[service]

    c1, c2, c3 = st.columns(3)

    c1.metric("Delay", f"{delay} ms")
    c2.metric("Jitter", f"{jitter} ms")
    c3.metric("Priority", priority)

# =====================================================
# PROTOCOL ANALYZER
# =====================================================
with tab6:

    st.header("Live Wireless Protocol Analyzer")

    rows = []

    event_list = [
        "GPRS Attach",
        "PDP Activation",
        "IMS Register",
        "Handoff",
        "AAA Authentication",
        "IPSec Tunnel Setup",
        "SIP Invite"
    ]

    for _ in range(15):

        rows.append([
            random.randint(100000, 999999),
            random.choice(event_list),
            random.choice([
                "Mobile",
                "BTS",
                "SGSN",
                "GGSN",
                "IMS"
            ]),
            random.choice([
                "IMS",
                "Internet",
                "AAA",
                "GGSN"
            ]),
            random.choice([
                "UDP",
                "TCP",
                "SIP",
                "IPSec"
            ])
        ])

    df = pd.DataFrame(
        rows,
        columns=[
            "Timestamp",
            "Event",
            "Source",
            "Destination",
            "Protocol"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

st.sidebar.title("About")
st.sidebar.info(
    "NetVerse-X demonstrates wireless network operations "
    "including GPRS, IMS, Mobility, Security and QoS "
    "based on Anna University FI1925 syllabus."
)
