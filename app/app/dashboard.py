import streamlit as st
import tempfile
import os
import pandas as pd

from app.ocr.extractor import extract_text
from app.extraction.invoice_fields import extract_invoice_data
from app.extraction.items.item_extractor import extract_line_items
from app.validation.invoice_validator import validate_total
from app.ml.feature_engineering import create_invoice_features
from app.ml.anomaly_detector import InvoiceAnomalyDetector
from app.llm.invoice_ai import InvoiceAI
from app.agent import InvoiceAgent


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Invoice Processing System",
    page_icon="🧾",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #777;
        margin-bottom: 30px;
    }

    .safe {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        background-color: #d4edda;
    }

    .danger {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        background-color: #f8d7da;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🧾 AI-Powered Invoice Processing</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'OCR • AI Extraction • Validation • ML Anomaly Detection • Gemini AI'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Processing Pipeline")

st.sidebar.write("✅ OCR")
st.sidebar.write("✅ Field Extraction")
st.sidebar.write("✅ Line Item Extraction")
st.sidebar.write("✅ Invoice Validation")
st.sidebar.write("✅ Feature Engineering")
st.sidebar.write("✅ ML Anomaly Detection")
st.sidebar.write("✅ Gemini AI Analysis")
st.sidebar.write("✅ Agent Decision")


# =========================================================
# FILE UPLOAD
# =========================================================

st.header("📤 Upload Invoice")

uploaded_file = st.file_uploader(
    "Choose an invoice image",
    type=["png", "jpg", "jpeg"]
)


# =========================================================
# PROCESS BUTTON
# =========================================================

if uploaded_file is not None:

    st.success(
        f"Invoice selected: {uploaded_file.name}"
    )

    if st.button(
        "🚀 Process Invoice",
        type="primary"
    ):

        # =================================================
        # SAVE TEMPORARY IMAGE
        # =================================================

        suffix = os.path.splitext(
            uploaded_file.name
        )[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(
                uploaded_file.getbuffer()
            )

            image_path = temp_file.name


        try:

            # =================================================
            # STEP 1 — OCR
            # =================================================

            with st.spinner("Reading invoice with OCR..."):

                ocr_text = extract_text(
                    image_path
                )

            st.success("OCR completed")


            # =================================================
            # STEP 2 — FIELD EXTRACTION
            # =================================================

            with st.spinner("Extracting invoice fields..."):

                invoice_data = extract_invoice_data(
                    ocr_text
                )

            st.success("Invoice fields extracted")


            # =================================================
            # STEP 3 — LINE ITEMS
            # =================================================

            with st.spinner("Extracting line items..."):

                line_items = extract_line_items(
                    ocr_text
                )

            st.success("Line items extracted")


            # =================================================
            # STEP 4 — VALIDATION
            # =================================================

            with st.spinner("Validating invoice..."):

                validation = validate_total(
                    invoice_data
                )

            st.success("Validation completed")


            # =================================================
            # STEP 5 — FEATURES
            # =================================================

            features = create_invoice_features(
                invoice_data,
                line_items
            )


            # =================================================
            # STEP 6 — ML ANOMALY DETECTION
            # =================================================

            with st.spinner(
                "Running ML anomaly detection..."
            ):

                detector = InvoiceAnomalyDetector()


                training_data = pd.DataFrame({

                    "subtotal": [
                        10000, 15000, 22000, 18000,
                        25000, 30000, 12000, 17000,
                        21000, 28000, 500000
                    ],

                    "tax": [
                        1800, 2700, 3960, 3240,
                        4500, 5400, 2160, 3060,
                        3780, 5040, 90000
                    ],

                    "total": [
                        11800, 17700, 25960, 21240,
                        29500, 35400, 14160, 20060,
                        24780, 33040, 590000
                    ],

                    "item_count": [
                        3, 4, 5, 3, 6,
                        5, 4, 3, 5, 6,
                        20
                    ],

                    "total_quantity": [
                        8, 10, 12, 7, 15,
                        11, 9, 8, 14, 16,
                        200
                    ],

                    "average_item_price": [
                        3333, 3750, 4400, 6000,
                        4166, 6000, 3000, 5666,
                        4200, 4666, 25000
                    ],

                    "tax_percentage": [
                        18, 18, 18, 18, 18,
                        18, 18, 18, 18, 18,
                        18
                    ]
                })


                detector.train(
                    training_data
                )


                X_current = pd.DataFrame(
                    [features]
                )


                anomaly_result = detector.predict(
                    X_current
                )


                result = anomaly_result[0]

                anomaly_status = result[
                    "status"
                ]

                anomaly_score = result[
                    "anomaly_score"
                ]


            # =================================================
            # STEP 7 — GEMINI AI
            # =================================================

            with st.spinner(
                "Generating AI invoice analysis..."
            ):

                ai = InvoiceAI()

                analysis = ai.analyze_invoice(

                    invoice_data,

                    line_items,

                    validation,

                    anomaly_status,

                    anomaly_score
                )


            # =================================================
            # STEP 8 — AGENT
            # =================================================

            with st.spinner(
                "Generating agent decision..."
            ):

                agent = InvoiceAgent()

                decision = agent.decide_action(

                    invoice_data,

                    validation,

                    anomaly_status,

                    anomaly_score,

                    None
                )


            # =================================================
            # FINAL STATUS
            # =================================================

            if (
                validation.get("status") == "VALID"
                and anomaly_status == "NORMAL"
            ):

                final_status = "SAFE"

            elif (
                validation.get("status") == "ANOMALY"
                or anomaly_status == "ANOMALY"
            ):

                final_status = "REVIEW REQUIRED"

            else:

                final_status = "REVIEW"


            # =================================================
            # RESULTS
            # =================================================

            st.markdown("---")

            st.header("📊 Invoice Report")


            # =================================================
            # STATUS
            # =================================================

            if final_status == "SAFE":

                st.markdown(
                    '<div class="safe">'
                    '✅ FINAL STATUS: SAFE'
                    '</div>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    '<div class="danger">'
                    '⚠️ FINAL STATUS: REVIEW REQUIRED'
                    '</div>',
                    unsafe_allow_html=True
                )


            st.markdown("---")


            # =================================================
            # INVOICE DETAILS
            # =================================================

            st.subheader(
                "📄 Invoice Details"
            )

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Vendor",
                invoice_data.get(
                    "vendor",
                    "N/A"
                )
            )

            col2.metric(
                "Invoice Number",
                invoice_data.get(
                    "invoice_number",
                    "N/A"
                )
            )

            col3.metric(
                "Invoice Date",
                invoice_data.get(
                    "invoice_date",
                    "N/A"
                )
            )

            col4.metric(
                "Due Date",
                invoice_data.get(
                    "due_date",
                    "N/A"
                )
            )


            # =================================================
            # FINANCIAL SUMMARY
            # =================================================

            st.subheader(
                "💰 Financial Summary"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Subtotal",
                f"₹{invoice_data.get('subtotal', 0):,.2f}"
            )

            col2.metric(
                "GST",
                f"₹{invoice_data.get('tax', 0):,.2f}"
            )

            col3.metric(
                "Total",
                f"₹{invoice_data.get('total', 0):,.2f}"
            )


            st.write(
                f"**GST Rate:** "
                f"{features.get('tax_percentage', 0):.2f}%"
            )


            # =================================================
            # LINE ITEMS
            # =================================================

            st.subheader(
                "📦 Line Items"
            )

            if line_items:

                items_df = pd.DataFrame(
                    line_items
                )

                st.dataframe(
                    items_df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.warning(
                    "No line items detected."
                )


            # =================================================
            # VALIDATION
            # =================================================

            st.subheader(
                "🔍 Invoice Validation"
            )

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Status",
                validation.get(
                    "status",
                    "UNKNOWN"
                )
            )

            col2.metric(
                "Expected Total",
                f"₹{validation.get('expected_total', 0):,.2f}"
            )

            col3.metric(
                "Difference",
                f"₹{validation.get('difference', 0):,.2f}"
            )


            # =================================================
            # ML ANALYSIS
            # =================================================

            st.subheader(
                "🤖 ML Anomaly Detection"
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Risk Status",
                anomaly_status
            )

            col2.metric(
                "Anomaly Score",
                anomaly_score
            )


            # =================================================
            # FEATURES
            # =================================================

            with st.expander(
                "📈 View ML Features"
            ):

                st.json(
                    features
                )


            # =================================================
            # OCR TEXT
            # =================================================

            with st.expander(
                "🔎 View OCR Text"
            ):

                st.text(
                    ocr_text
                )


            # =================================================
            # GEMINI ANALYSIS
            # =================================================

            st.subheader(
                "🧠 Gemini AI Analysis"
            )

            st.info(
                analysis
            )


            # =================================================
            # AGENT DECISION
            # =================================================

            st.subheader(
                "🤖 Agent Decision"
            )

            st.warning(
                decision
            )


            # =================================================
            # SUCCESS MESSAGE
            # =================================================

            st.success(
                "🎉 Invoice processing completed successfully!"
            )


        except Exception as e:

            st.error(
                "Invoice processing failed."
            )

            st.exception(e)


        finally:

            # =================================================
            # DELETE TEMPORARY FILE
            # =================================================

            if os.path.exists(
                image_path
            ):

                os.remove(
                    image_path
                )


else:

    st.info(
        "👆 Upload an invoice image above to begin."
    )

    st.markdown("---")

    st.subheader(
        "How it works"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.write(
        "📷 **1. Upload**\n\n"
        "Upload your invoice image."
    )

    col2.write(
        "🔍 **2. Extract**\n\n"
        "OCR and AI extract invoice information."
    )

    col3.write(
        "🤖 **3. Analyze**\n\n"
        "ML detects unusual invoices."
    )

    col4.write(
        "📊 **4. Report**\n\n"
        "Get a complete invoice report."
    )
