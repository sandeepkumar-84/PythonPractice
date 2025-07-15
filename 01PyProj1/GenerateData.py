from datasets import load_dataset
import pandas as pd
#ds = load_dataset("bot-remains/student-assistance-chatbot")
df = pd.read_json("https://datasets/bot-remains/student-assistance-chatbot/data-set.json")
def generate_data():
    # Save the dataset to a local file
    #ds.save_to_disk("student_assistance_chatbot_data") 
    #generate on local machine and wrap in generate_data() function
    df = df.rename(columns={"question": "input", "answer": "output"})
    df = df[["input", "output"]]        
    # Save the DataFrame to a CSV file
    df.to_csv("student_assistance_chatbot_data.csv", index=False)  
    
if __name__ == "__main__":
    ##generate_data()
    generate_data()
    print("Data generation complete. Dataset saved to 'student_assistance_chatbot_data'.")  

 

       

 
