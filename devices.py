import pyaudio

p = pyaudio.PyAudio()

print("Available devices:")
for i in range(p.get_device_count()):
    device_name = p.get_device_info_by_index(i)["name"]
    print(f"- {i}: {device_name}")