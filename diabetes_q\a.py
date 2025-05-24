import re

# Knowledge base for diabetes-related questions
knowledge_base = {
    r"(what is|define|tell me about) diabetes": 
        "Diabetes is a chronic condition where the body cannot properly regulate blood sugar (glucose) levels. It occurs when the pancreas doesn't produce enough insulin (a hormone that regulates blood sugar) or when the body can't effectively use the insulin it produces. There are three main types: Type 1, Type 2, and gestational diabetes.",
    
    r"(what are the types|kinds of diabetes)": 
        "There are three main types of diabetes:\n1. **Type 1 Diabetes**: An autoimmune condition where the body attacks insulin-producing cells in the pancreas, usually diagnosed in children or young adults. Insulin injections are required.\n2. **Type 2 Diabetes**: The body becomes resistant to insulin or doesn't produce enough, often linked to lifestyle factors like obesity. It's more common in adults and can often be managed with diet, exercise, and medication.\n3. **Gestational Diabetes**: Develops during pregnancy and usually resolves after childbirth, but increases the risk of Type 2 diabetes later.",
    
    r"(symptoms|signs) of diabetes": 
        "Common symptoms of diabetes include increased thirst, frequent urination, extreme fatigue, blurred vision, slow-healing wounds, and unexplained weight loss. Type 1 symptoms often appear suddenly, while Type 2 symptoms develop gradually.",
    
    r"(cause|causes|why do people get) diabetes": 
        "Causes vary by type:\n- **Type 1**: Autoimmune reaction, possibly triggered by genetics or environmental factors like viruses.\n- **Type 2**: Often linked to genetics, obesity, sedentary lifestyle, and insulin resistance.\n- **Gestational**: Hormonal changes during pregnancy can cause insulin resistance, especially in those with risk factors like obesity.",
    
    r"(treat|manage|management|how to control) diabetes": 
        "Management depends on the type:\n- **Type 1**: Daily insulin injections or an insulin pump, blood sugar monitoring, healthy diet, and exercise.\n- **Type 2**: Lifestyle changes (healthy diet, regular exercise), oral medications, and sometimes insulin.\n- **Gestational**: Diet, exercise, and sometimes insulin or medication. Regular monitoring is key, and consulting a healthcare provider is essential.",
    
    r"(diet|food|what to eat) for diabetes": 
        "A diabetes-friendly diet includes whole grains, vegetables, lean proteins, and healthy fats. Focus on low-glycemic foods, control portion sizes, and limit refined sugars and processed carbs. Consult a dietitian for a personalized plan.",
    
    r"(complications|risks|dangers) of diabetes": 
        "Uncontrolled diabetes can lead to complications like heart disease, stroke, kidney damage, nerve damage (neuropathy), eye damage (retinopathy), and foot problems. Regular monitoring and management reduce these risks.",
    
    r"(difference between type 1 and type 2|type 1 vs type 2)": 
        "Type 1 diabetes is an autoimmune condition where the body stops producing insulin, often diagnosed in youth, requiring insulin therapy. Type 2 diabetes involves insulin resistance or insufficient insulin production, is more common in adults, and is often linked to lifestyle factors. It can sometimes be managed without insulin.",
    
    r"(prevent|prevention|how to avoid) diabetes": 
        "Type 1 diabetes cannot be prevented. For Type 2, you can reduce risk by maintaining a healthy weight, eating a balanced diet, exercising regularly, and avoiding smoking. Regular check-ups help with early detection.",
    
    r"(blood sugar|glucose) (level|range|normal)": 
        "Normal blood sugar levels vary: fasting (before meals) should be 70-99 mg/dL, and 1-2 hours after meals, less than 140 mg/dL. For diabetics, target ranges may be higher (e.g., 80-130 mg/dL fasting). Always consult a doctor for personalized targets."
}

# Function to find the best matching response
def get_response(user_input):
    user_input = user_input.lower().strip()
    if user_input in ["exit", "quit", "bye"]:
        return "Goodbye! Stay healthy and consult a healthcare professional for personalized advice."
    
    for pattern, response in knowledge_base.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "Sorry, I don't have information on that. Please ask another question about diabetes or type 'exit' to quit."

# Main chatbot loop
def diabetes_chatbot():
    print("Welcome to the Diabetes Information Chatbot!")
    print("Ask me anything about diabetes (e.g., symptoms, types, management). Type 'exit' to quit.")
    print("Note: This chatbot provides general information. Always consult a doctor for medical advice.\n")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response, "\n")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break

# Run the chatbot
if __name__ == "__main__":
    diabetes_chatbot()
