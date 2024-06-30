import os
import sys
import shutil
import logging
import gzip
import argparse
import datetime

def setup_logging(log_dir):
    if not os.path.exists(log_dir):
        print(f"{log_dir} does not exist.")
        ans = input(f"Would you like to create the {log_dir} directory(Y/N):").strip()
        if ans.lower() not in ['y','n']:
            print("Enter a valid answer")
            sys.exit(1)
        if ans.lower() == 'y':
            os.makedirs(log_dir)
        else:
            sys.exit(1)
    log_file = os.path.join(log_dir,'rotation.log')    
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file)

def rotation_tool(log_dir,max_size,max_file):
    try:
        print(log_dir,max_size,max_file)
        logs = [os.path.join(log_dir,f) for f in os.listdir(log_dir) if f.endswith(".log")]
        logs.sort(key=os.path.getmtime)
        print("Welcome to logging rotation tool")

        for log in logs:
            if os.path.getsize(log) > max_size:
                with open(log,'rb') as f_in:
                    with gzip.open(f"{log}.gz",'wb') as f_out:
                        shutil.copyfileobj(f_in,f_out)
                with open(log,'w') as f:
                    f.truncate(0)
                logging.info(f"Compressed {log}")
                print(f"Compressed {log}")

        if len(logs) > max_file:
            for log in logs[:len(logs) - max_file]:
                if os.path.getsize(log) < max_size:
                    continue
                with open(log,'rb') as f_in:
                    with gzip.open(f"{log}.gz",'wb') as f_out:
                        shutil.copyfileobj(f_in,f_out)
                with open(log,'w') as f:
                    f.truncate(0)
                logging.info(f"Compressed {log}")
                print(f"Compressed {log}")

        logs = [os.path.join(log_dir,f) for f in os.listdir(log_dir) if f.endswith(".gz")]
        logs.sort(key=os.path.getmtime)
        if len(logs) > max_file:
            logs_to_remove = len(logs) - max_file
            for log in logs[:logs_to_remove]:
                os.remove(log)
                logging.info(f"{log} removed.")
                print(f"{log} removed.")
        print("Log rotation done.")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Error found: {e}")
        print(f"Error found: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_dir',type=str,required=True,help="Directory where logs are present")
    parser.add_argument("--max_size",type=int,default=10*1024*1024,help="Max size of log files")
    parser.add_argument("--max_file",type=int,default=5,help="Maximum log files allowed")

    args = parser.parse_args()

    if args.max_size <= 0:
        print("Error: max_size must be a positive integer.")
        sys.exit(1)

    if args.max_file <= 0:
        print("Error: max_files must be a positive integer.")
        sys.exit(1)

    setup_logging(args.log_dir)
    rotation_tool(args.log_dir,args.max_size,args.max_file)

if __name__ =="__main__":
    main()