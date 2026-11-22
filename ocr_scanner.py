"""
NutriTrack Core - OCR Nutrition Label Parser Module
Author: D. Williams
Course: ITCS 2080 - Fundamentals of Software Engineering (Fall 2026)
"""

import json
import re
from datetime import datetime, timezone


class NutritionLabelScanner:
    """Parses raw OCR text from food packaging into structured nutritional data."""

    SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")
    MAX_PAYLOAD_MB = 5.0

    def __init__(self, user_id: str, unit_system: str = "imperial"):
        if not user_id or not user_id.isalnum():
            raise ValueError("Invalid alphanumeric user_id provided.")
        self.user_id = user_id
        self.unit_system = unit_system.lower()

    def validate_image_metadata(self, filename: str, file_size_mb: float) -> bool:
        """Validates file extension and payload size before cloud processing."""
        if not filename.lower().endswith(self.SUPPORTED_FORMATS):
            raise ValueError(f"Unsupported image format: {filename}")
        if file_size_mb <= 0 or file_size_mb > self.MAX_PAYLOAD_MB:
            raise ValueError(f"Image size must be between 0 and {self.MAX_PAYLOAD_MB} MB.")
        return True

    def parse_ocr_text(self, raw_text: str) -> dict:
        """Extracts calories, protein, carbs, and fats from raw OCR strings."""
        patterns = {
            "calories": r"Calories\s*[:\-]?\s*(\d+)",
            "protein_g": r"Protein\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g",
            "carbs_g": r"Total Carbohydrate\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g",
            "fat_g": r"Total Fat\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*g",
        }

        extracted = {}
        for nutrient, pattern in patterns.items():
            match = re.search(pattern, raw_text, re.IGNORECASE)
            extracted[nutrient] = float(match.group(1)) if match else 0.0

        return {
            "user_id": self.user_id,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "unit_system": self.unit_system,
            "nutrients": extracted,
            "sync_status": "QUEUED_FOR_SYNC",
        }


if __name__ == "__main__":
    sample_ocr_output = """
    Nutrition Facts
    Serving Size 1 cup (228g)
    Calories 250
    Total Fat 12g
    Total Carbohydrate 31g
    Protein 5g
    """

    scanner = NutritionLabelScanner(user_id="dwilliams01")
    if scanner.validate_image_metadata("cereal_box.jpg", file_size_mb=1.8):
        parsed_entry = scanner.parse_ocr_text(sample_ocr_output)
        print(json.dumps(parsed_entry, indent=2))
