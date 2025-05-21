
import random
def simulate_sensor_data():
    return {
        "pH": round(random.uniform(6.5, 8.0), 2),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "dissolved_oxygen": round(random.uniform(5.0, 9.0), 2)
    }
def analyze_data(data):
    alerts = []
    if data["pH"] < 6.8 or data["pH"] > 7.8:
        alerts.append("⚠️ pH is outside optimal range (6.8–7.8)")
    if data["temperature"] < 22 or data["temperature"] > 28:
        alerts.append("⚠️ Temperature is outside optimal range (22°C–28°C)")
    if data["dissolved_oxygen"] < 6:
        alerts.append("⚠️ Dissolved oxygen is low (<6 mg/L)")
    return alerts if alerts else ["✅ All conditions are within safe range"]
# --- Chatbot Interaction (Command-line based) ---
def chatbot():
    print("\n🤖 AquaWatch Chatbot - Type 'exit' to stop.")
    while True:
        user_input = input("You: ").lower()
        if "pH" in user_input:
            print("Bot: pH should be between 6.8 and 7.8.")
        elif "temperature" in user_input:
            print("Bot: Ideal temperature range is 22°C to 28°C.")
        elif "oxygen" in user_input or "do" in user_input:
            print("Bot: Maintain DO above 6 mg/L.")
        elif "exit" in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")
# --- Main Program ---
if __name__ == "__main__":
    print("🌊 AquaWatch Monitoring System - Console Demo")
    sensor_data = simulate_sensor_data()
    print(f"\nSensor Data: {sensor_data}")
    alerts = analyze_data(sensor_data)
    print("\nAI Analysis:")
    for alert in alerts:
        print(alert)
    chatbot()
