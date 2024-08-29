import requests

def upload_file(file_path):
    url = 'http://192.168.1.148:8000'
    files = {'file': open(file_path, 'rb')}

    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("File uploaded successfully:", response.text)
        else:
            print(f"Error response: {response.text}")
            print(f"Failed to upload file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        files['file'].close()

# Example usage
file_path = './local/file.txt'
upload_file(file_path)