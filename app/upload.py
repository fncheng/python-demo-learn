from flask import Blueprint, make_response, jsonify, request
import os

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload/single", methods=["POST"])
def upload():
    # 检查请求中是否包含文件部分
    if "file" not in request.files:
        return "No file part in the request", 400

    file = request.files.get("file")

    if file:
        filename = file.filename

        print("****filename****", filename)
        final_path = os.path.join("./upload/", filename)
        os.makedirs(os.path.dirname(final_path), exist_ok=True)
        if not os.path.exists(final_path):
            file.save(final_path)
            response = make_response(
                jsonify({"message": "File uploaded successfully"}), 200
            )
            return response
        else:
            print(f"File {filename} already exists")
            return jsonify({"error": "File already exists"}), 200

    return "No file uploaded", 400
