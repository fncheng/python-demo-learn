from flask import Flask, request, jsonify, make_response, Response
from flask_cors import CORS
import os
import time

app = Flask(__name__)
CORS(app)


@app.route("/upload", methods=["POST"])
def upload_file():
    # 获取文件名和开始字节
    # file_name = request.headers.get('File-Name')
    chunk = request.files.get("chunk")
    chunk_index = request.form.get("chunkIndex")
    file_hash = request.form.get("fileHash")

    # print('file_name', file_name)

    if not chunk or chunk_index is None or not file_hash:
        return jsonify({"error": "Invalid request"}), 400

    # start_byte = int(request.headers.get('Start-Byte'))
    chunk_index = int(chunk_index)
    chunk_filename = f"{chunk_index}.part"
    final_path = os.path.join("./upload/", file_hash, chunk_filename)
    os.makedirs(os.path.dirname(final_path), exist_ok=True)
    chunk.save(final_path)

    # 打开文件（如果文件不存在则创建）
    # with open(os.path.join('./upload/', file_hash), 'ab') as f:
    #     # 移动到开始字节的位置
    #     f.seek(start_byte)
    #     # 将上传的数据写入文件
    #     f.write(request.data)

    return jsonify({"message": "Upload successful"}), 200


@app.route("/upload/check", methods=["GET"])
def check_chunk():
    chunk_path = os.path.join(
        "./upload/",
        request.args.get("fileHash"),
    )
    print("chunk_path**", chunk_path)
    # request.args.get("chunkIndex") + ".part",

    chunk_indices = []
    for filename in os.listdir(chunk_path):
        try:
            index = int(filename.split(".")[0])
            print("index***", index)
            chunk_indices.append(index)
        except ValueError:
            pass  # 忽略无法转换为整数的文件名
    print("*****", chunk_indices)
    return sorted(chunk_indices)


@app.route("/upload/merge", methods=["POST"])
def merge_chunks():
    file_hash = request.json["fileHash"]
    output_dir = "./merged_files/"
    input_dir = "./upload/"
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 获取分片目录
    chunk_dir = os.path.join(input_dir, file_hash)
    # 获取所有分片文件的路径并按文件名排序
    chunk_files = sorted(
        [f for f in os.listdir(chunk_dir) if f.endswith(".part")],
        key=lambda x: int(x.split(".")[0]),
    )
    # 合并分片文件
    with open(os.path.join(output_dir, file_hash), "wb") as outfile:
        for chunk_file in chunk_files:
            chunk_path = os.path.join(chunk_dir, chunk_file)
            with open(chunk_path, "rb") as chunk_f:
                outfile.write(chunk_f.read())

    # 删除分片文件
    # for chunk_file in chunk_files:
    #     chunk_path = os.path.join(chunk_dir, chunk_file)
    #     os.remove(chunk_path)

    return jsonify({"message": "上传成功！"}), 200


@app.route("/test/getName", methods=["GET"])
def get_name():
    time.sleep(2)
    # response = make_response(jsonify({"name": "John Doe"}), 200)
    response = Response(
        response='{"name": "Jonn Doe"}', status=200, mimetype="application/json"
    )
    return response


@app.route("/test/getNumber", methods=["GET"])
def get_number():
    time.sleep(3)
    response = make_response(jsonify({"number": 999}), 200)
    response.headers.set("X-Custom-Header", "Test")
    return response


@app.route("/test/getPieData", methods=["GET"])
def get_pie_data():
    time.sleep(2)
    data = [
        {"value": 1048, "name": "Search Engine"},
        {"value": 735, "name": "Direct"},
        {"value": 580, "name": "Email"},
        {"value": 484, "name": "Union Ads"},
        {"value": 300, "name": "Video Ads"},
    ]
    response = make_response(jsonify(data), 200)
    return response


@app.route("/test/getContent", methods=["GET"])
def get_content():
    content = {
        "type": 16,
        "transcriptResult": '{"ps":[{"lastPsRole":"","pTime":[970,15980],"role":"0","words":[{"modal":false,"rl":"0","text":"这个","time":[970,1120],"wp":"n"},{"modal":false,"rl":"0","text":"就","time":[1130,1240],"wp":"n"},{"modal":false,"rl":"0","text":"可以","time":[1250,1640],"wp":"n"},{"modal":false,"rl":"0","text":"了","time":[1690,2320],"wp":"n"},{"modal":false,"rl":"0","text":"，","time":[2370,2370],"wp":"p"},{"modal":false,"rl":"0","text":"叫","time":[2370,2560],"wp":"n"},{"modal":false,"rl":"0","text":"什么","time":[2570,3000],"wp":"n"},{"modal":false,"rl":"0","text":"？","time":[3640,3640],"wp":"p"},{"modal":false,"rl":"0","text":"产品","time":[3640,4230],"wp":"n"},{"modal":false,"rl":"0","text":"目标","time":[4240,4630],"wp":"n"},{"modal":false,"rl":"0","text":"是","time":[4640,4830],"wp":"n"},{"modal":false,"rl":"0","text":"打造","time":[4840,5350],"wp":"n"},{"modal":false,"rl":"0","text":"一个","time":[5360,5910],"wp":"n"},{"modal":false,"rl":"0","text":"用户","time":[5920,6350],"wp":"n"},{"modal":false,"rl":"0","text":"友好","time":[6360,6750],"wp":"n"},{"modal":false,"rl":"0","text":"的","time":[6760,6950],"wp":"n"},{"modal":false,"rl":"0","text":"前端","time":[6960,7310],"wp":"n"},{"modal":false,"rl":"0","text":"界面","time":[7360,7750],"wp":"n"},{"modal":false,"rl":"0","text":"，","time":[7760,7760],"wp":"p"},{"modal":false,"rl":"0","text":"用户","time":[7760,8190],"wp":"n"},{"modal":false,"rl":"0","text":"只需","time":[8200,8510],"wp":"n"},{"modal":false,"rl":"0","text":"上传","time":[8520,8910],"wp":"n"},{"modal":false,"rl":"0","text":"会议","time":[8920,9310],"wp":"n"},{"modal":false,"rl":"0","text":"音频","time":[9320,9670],"wp":"n"},{"modal":false,"rl":"0","text":"文件","time":[9680,10070],"wp":"n"},{"modal":false,"rl":"0","text":"，","time":[10330,10330],"wp":"p"},{"modal":false,"rl":"0","text":"即可","time":[10330,10840],"wp":"n"},{"modal":false,"rl":"0","text":"通过","time":[10850,11320],"wp":"n"},{"modal":false,"rl":"0","text":"智能","time":[11330,11560],"wp":"n"},{"modal":false,"rl":"0","text":"体","time":[11570,11720],"wp":"n"},{"modal":false,"rl":"0","text":"自动","time":[11730,12120],"wp":"n"},{"modal":false,"rl":"0","text":"生成","time":[12130,12520],"wp":"n"},{"modal":false,"rl":"0","text":"会议","time":[12530,12880],"wp":"n"},{"modal":false,"rl":"0","text":"纪要123","time":[12890,13440],"wp":"n"},{"modal":false,"rl":"0","text":"，","time":[15270,15270],"wp":"p"},{"modal":false,"rl":"0","text":"一模一样","time":[15270,15980],"wp":"n"}],"key":"39df8e84-ff0b-4471-888d-f25ed2e3d66c"}],"roles":[],"styles":[]}',
        "saveTime": 1735635763000,
        "version": 1735635763585,
        "hjFrom": 25,
        "languageType": 1,
    }
    response = make_response(content, 200)
    return response


@app.route("/events", methods=["GET"])
def events():
    def generate():
        def send_data(event, data):
            return f"event: {event}\ndata: {data}\n\n"

        try:
            yield send_data("message", "Connected")
            time.sleep(1)
            yield send_data(
                "message",
                "\u53ef\u80fd\u4f1a\u5728\u540e\u7eed\u7684\u6570\u636e\u6e32\u67d3\u65f6\u51fa\u73b0\u4e0d\u5fc5\u8981\u7684\u91cd\u590d\u64cd\u4f5c\uff0c",
            )
            time.sleep(1)
            yield send_data(
                "message",
                "如果你想要对消息进行更细粒度的控制，比如添加时间戳、作者信息等，可以将每个消息包装成一个更复杂的 HTML 元素。",
            )
            time.sleep(2)
            yield send_data("message", "[DONE]")
        except GeneratorExit:
            print("Client disconnected")

    response = make_response(generate(), 200)
    response.headers.set("Content-Type", "text/event-stream")
    response.headers.set("Cache-Control", "no-cache")
    response.headers.set("Connection", "keep-alive")

    return response


if __name__ == "__main__":
    if not os.path.exists("./upload"):
        os.makedirs("./upload")
    app.run(port=3000, debug=True)
