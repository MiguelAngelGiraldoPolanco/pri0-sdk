# from pri0.pri0 import Sanitizer


# def test_sanitizer_long_text_stress_matrix():
#     """
#     Long Text Integration Test: Verifies that the engine processes
#     a large volume of text with multiple mixed real-world data types
#     without breaking the text structure or causing infinite loops.
#     """
#     # Initialize the sanitizer exactly with your current production setup
#     sanitizer = Sanitizer(mode="local")

#     # A long, realistic payload matching production log patterns
#     long_dirty_payload = (
#         "Dear team, please find attached the data for the security audit.\n"
#         "The primary user has the ID DNI3301543B and their contact phone number "
#         "in Spain is 612345678, although it sometimes appears in logs as "
#         "tel: 612345678 or stuck inside complex strings like user 612345678.\n"
#         "On the other hand, transactions were made from the bank account "
#         "with IBAN ES13004@9437..67123 10031424 234234 completely as normal.\n"
#         "For any inquiries, you can send an email to technical support at "
#         "secure contact@company.com or review the docs at https://api.pvt.\n"
#         "The verification process completed successfully for CIF A58818501.\n"
#         "End of massive integration report."
#     )

#     # Execute your original mask method with Spain and common patterns
#     masked_output = sanitizer.mask(
#         text=long_dirty_payload,
#         countries=["ES"],
#         common=["COMMON_EMAIL", "COMMON_URL"],
#     )

#     # =====================================================================
#     # ASSERTIONS (VALIDATING AGAINST YOUR PRODUCTION CORE)
#     # =====================================================================

#     # 1. Total Security: No real private data survives in the long text
#     assert "33011543B" not in masked_output
#     assert "612345678" not in masked_output
#     assert "ES1300494376712310031424" not in masked_output
#     assert "contact@company.com" not in masked_output
#     assert "A58818501" not in masked_output

#     # 2. Precision: Verify that your SDK's actual labels are injected properly
#     assert "[ES_DNI_NIF]" in masked_output
#     assert "[ES_IBAN]" in masked_output
#     assert "[COMMON_EMAIL]" in masked_output
#     assert "[ES_CIF]" in masked_output

#     # 3. Structural Integrity of Long Text
#     # Your code must keep legitimate words and paragraph structures untouched
#     assert "Dear team, please find attached the data" in masked_output
#     assert "End of massive integration report." in masked_output
#     assert "\n" in masked_output  # Line breaks are preserved perfectly
