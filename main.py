import streamlit as st

# Define the tests and their maximum scores
tests = {
    "Serpentine": 50, "Right Turn": 50, "Rear Duals Clearance": 50,
    "1st Customer Stop": 50, "Right Hand Reverse": 50, "Offset Street": 50,
    "Left Hand Reverse": 50, "Left Turn": 50, "2nd Customer Stop": 50,
    "Diminishing Clearance": 50, "Judgment Stop": 50, "Safety Habits": 50,
    "Smoothness of Operation": 50, "Vehicle Inspection": 50
}

def calculate_total_score(scores):
    return sum(scores.values())

if __name__ == "__main__":
    st.set_page_config(page_title="Bus Roadeo Scoring App", layout="wide")

    st.title("Bus Roadeo Scoring App")

    participant_name = st.text_input("Participant Name")

    scores = {test: 0 for test in tests}

    # Create tabs for each test
    tabs = st.tabs(list(tests.keys()))
    for i, test in enumerate(tests):
        with tabs[i]:
            scores[test] = st.number_input(f"Score for {test} (Max {tests[test]} points)", min_value=0, max_value=tests[test], key=test)

    if st.button("Calculate Total Score"):
        total_score = calculate_total_score(scores)
        st.write(f"Total Score for {participant_name}: {total_score}")

        # Display individual scores
        st.write("Scores by Test:")
        for test, score in scores.items():
            st.write(f"{test}: {score}")
