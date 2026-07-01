class SummarizeService:
    def generate_summary(self, text: str) -> str:
        return f"Ringkasan dari: {text.upper()}"
    
service = SummarizeService()