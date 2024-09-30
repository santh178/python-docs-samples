# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Vertex AI sample for verifying if an image contains a
    digital watermark. By default, a non-visible, digital watermark (called a
    SynthID) is added to images generated by a model version that supports
    watermark generation.
"""
import os

from vertexai.preview import vision_models

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


def verify_image_watermark(
    input_file: str,
) -> vision_models.WatermarkVerificationResponse:
    # [START generativeaionvertexai_imagen_verify_image_watermark]

    import vertexai
    from vertexai.preview.vision_models import (
        Image,
        WatermarkVerificationModel,
    )

    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # input_file = "input-image.png"

    vertexai.init(project=PROJECT_ID, location="us-central1")

    verification_model = WatermarkVerificationModel.from_pretrained(
        "imageverification@001"
    )
    image = Image.load_from_file(location=input_file)

    watermark_verification_response = verification_model.verify_image(image)

    print(
        f"Watermark verification result: {watermark_verification_response.watermark_verification_result}"
    )
    # Example response:
    # Watermark verification result: ACCEPT
    # or "REJECT" if the image does not contain a digital watermark.

    # [END generativeaionvertexai_imagen_verify_image_watermark]
    return watermark_verification_response


if __name__ == "__main__":
    verify_image_watermark("test_resources/dog_newspaper.png")