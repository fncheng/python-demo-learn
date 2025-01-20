from flask import Blueprint, make_response, jsonify, request, send_file
import os

upload_bp = Blueprint("upload", __name__)


# 单个文件上传
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


@upload_bp.route("/status/<int:id>", methods=["GET"])
def status(id):
    print("id****", id)
    if id == 1:
        return jsonify({"status": "success"}), 200
    elif id == 2:
        return jsonify({"status": "failed"}), 200
    else:
        return jsonify({"status": "unknown"}), 200


@upload_bp.route("/upload/delete", methods=["POST"])
def delete_file():
    id = request.json.get("id")

    return jsonify({"message": "File deleted successfully"}), 200


# 获取文件列表
@upload_bp.route("/upload/list", methods=["GET"])
def list_files():
    files = os.listdir("./upload/")
    list = [{"id": i, "audioName": f} for i, f in enumerate(files)]
    return jsonify({"data": list}), 200


# 获取单个音频文件
@upload_bp.route("/audio/get/<string:audio_id>", methods=["GET"])
def get_audio(audio_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(current_dir, "../audios", f"{audio_id}.mp3")

    if os.path.exists(audio_path):
        file_size = os.path.getsize(audio_path)
        response = make_response(send_file(audio_path, mimetype="audio/mpeg"), 200)

        response.headers.set("Content-Length", file_size)
        response.headers.set("Content-Range", f"bytes 0-{file_size-1}/{file_size}")
        response.headers.set(
            "Content-Disposition", f'attachment; filename="{audio_id}.mp3"'
        )
        # response.headers.set("Content-Type", "application/octet-stream;charset=UTF-8")
        response.headers.set("Accept-Ranges", "bytes")
        return response
    else:
        return jsonify({"error": "File not found"}), 404
