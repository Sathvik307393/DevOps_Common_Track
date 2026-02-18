import os
import time

def detect_file_change(file_path, interval=1):
    last_modified = os.path.getmtime(file_path)
    last_position = 0
    while True:
        try:
            current_modified = os.path.getmtime(file_path)
            if current_modified != last_modified:
                with open("file.txt", 'r') as f:
                    f.seek(last_position)
                    new_data = f.read()
                    if new_data:
                        print("New Content has been added",new_data)
                        # print(new_data, end =" ")
                    last_position = f.tell()
                last_modified = current_modified
                print("File has undergone changes")
            time.sleep(interval)
        
        except OSError as e:
            print(f"Error is {e}")
            break
        
        except KeyboardInterrupt:
            print("Keyboard interuppted to close")
    
detect_file_change("file.txt")