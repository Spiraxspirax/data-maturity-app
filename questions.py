
# questions.py

domains = {
    "Governance": [
        "Do you have a documented data governance policy?",
        "Are data ownership roles assigned and communicated?",
        "Is there an operating model for governance enforcement?"
    ],
    "Quality": [
        "Are critical data elements regularly profiled for quality?",
        "Do you have automated alerts for data quality issues?",
        "Is there a team responsible for data quality remediation?"
    ],
    "Metadata": [
        "Do you catalog datasets with business-friendly terms?",
        "Is metadata updated automatically or manually?",
        "Can users easily find data via metadata search?"
    ],
    "Ownership": [
        "Do stewards sign off on data quality KPIs?",
        "Is there a RACI defined for every data domain?",
        "Are escalation paths in place for ownership issues?"
    ],
    "Architecture": [
        "Do you maintain an enterprise data model?",
        "Are integrations mapped in a lineage view?",
        "Is master/reference data managed centrally?"
    ],
    "Literacy": [
        "Do employees undergo data literacy training?",
        "Are there champions for data across business units?",
        "Are business glossaries widely adopted?"
    ],
    "Usage": [
        "Are data assets used to support business decisions?",
        "Is usage tracked for each published dataset?",
        "Are analytics self-serve with proper controls?"
    ]
}
