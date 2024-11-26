import csv



def convert_time(seconds):
    """
    Convert from seconds to hh:mm:ss,ms format.
    """
    ms = int((seconds % 1) * 1000)
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02},{ms:03}"

def csv_to_srt(input_csv, output_srt):
    """
    Convert CSV to SRT
    """
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        
        reader = csv.reader(csv_file)
        #skip headline
        next(reader)
        with open(output_srt, 'w', encoding='utf-8') as srt_file:
            for i, row in enumerate(reader):
                
                text = row[0]  
                start_time = convert_time(float(row[1])) 
                end_time = convert_time(float(row[2]))    
                                           
                # Save to SRT
                srt_file.write(f"{i + 1}\n")
                srt_file.write(f"{start_time} --> {end_time}\n")
                srt_file.write(f"{text.strip()}\n\n")

def main():
    csv_to_srt('transcription.csv', 'VIDEO.srt')

main()
