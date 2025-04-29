import os
import time
import json
import librosa
import torch
import subprocess
import 
from log_writer
import write_log
from pydub 
import AudioSegment
import shutil

# 경로 설정
ROOT_DIR = 
LOG_DIR = 
DATA_DIR = 
NODES_DIR =

# 모델 로드
processor = AutoProcessor
model =

def load_node_module(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()
    module_dict = {}
    exec(code, module_dict)
    return module_dict

# 노드 리셋
def reset_nodes():
    for layer in range(1, 6):
        layer_dir = os.path.join(NODES_DIR, f"Layer{layer}")
        if os.path.exists(layer_dir):
            shutil.rmtree(layer_dir)
            print(f"레이어 {layer} 노드 삭제 완료")
        os.makedirs(layer_dir, exist_ok=True)

# 노드 생성
def generate_nodes():
    print("SJPU 3D 노드 생성 시작...")
    try:
        subprocess.run
        print("SJPU 3D 노드 생성 완료")
        return True
    except subprocess.CalledProcessError as e:
        print(f"노드 생성 오류: {e}")
        return False

# 테스트 실행
def run_test(batch_size=10):
    os.makedirs(LOG_DIR, exist_ok=True)
    audio_files = [f for f in os.listdir(DATA_DIR) if f.endswith((".wav", ".m4a"))][:10]
    if not audio_files:
        return False

    emotion_map = {

            continue
        wav_path = audio_path
        if audio_file.endswith(".m4a"):
            try:
                wav_path = convert_m4a_to_wav(audio_path)
            except Exception as e:
                print(f"M4A 변환 오류: {audio_file}, {e}")
                continue
        try:
            audio, sr = librosa.load(wav_path, sr=16000)
                 
            response = model.generate(**inputs, max_length=1024)
            text = processor.batch_decode(response, skip_special_tokens=True)[0].lower()
            emotion = "중립"  # 기본값
            for key, value in emotion_map.items():
                if key in text:
                    emotion = value
                    break
            qwen_data = {"text": text, "emotion": emotion}


            layer_3_dir = os.path.join(NODES_DIR, "Layer3")
            layer_3_nodes = []
            for z_folder in os.listdir(layer_3_dir):
                z_folder_path = os.path.join(layer_3_dir, z_folder)
                if os.path.isdir(z_folder_path):
                    for node in os.listdir(z_folder_path):
                        layer_3_nodes.append(os.path.join(z_folder_path, node))
            if not layer_3_nodes:
                print(f"Layer 3 노드가 없습니다.")
                return False
            
            for node in layer_3_nodes[:1]:
                try:
                    module = load_node_module(node)
                    result = module["start_flow"](initial_vals, weight)
                    log_data = {"qwen_data": qwen_data, "sjpu_result": result}
                    write_log("test", log_data)
                except Exception as e:
                    print(f"노드 처리 오류: {node}, {e}")
                    return False
        except Exception as e:
            print(f"오디오 처리 오류: {wav_path}, {e}")
            return False
    return True

# 메인 실행
if __name__ == "__main__":
    if not generate_nodes():
        print("노드 생성 실패, 리셋 후 재시도...")
        reset_nodes()
        generate_nodes()
    if run_test():
        print("테스트 성공!")
    else:
        print("테스트 실패, 노드 리셋 후 종료...")
        reset_nodes()
