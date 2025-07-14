import requests

def fetch_leetcode_stats():
    username = "NevroHelios"
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "status" in data and data["status"] == "error":
            print("❌ Error:", data.get("message", "Unknown error"))
            return

        print(f"\n📊 LeetCode Stats for @{username}\n")
        print(f"✅ Total Solved     : {data.get('totalSolved')} / {data.get('totalQuestions')}")
        print(f"📘 Easy            : {data.get('easySolved')} / {data.get('totalEasy')}")
        print(f"📙 Medium          : {data.get('mediumSolved')} / {data.get('totalMedium')}")
        print(f"📕 Hard            : {data.get('hardSolved')} / {data.get('totalHard')}")
        print(f"📈 Acceptance Rate : {data.get('acceptanceRate')}%")
        print(f"🏆 Ranking         : {data.get('ranking')}")
        print(f"🎯 Contribution Points: {data.get('contributionPoints')}")
        print(f"🧠 Reputation      : {data.get('reputation')}")
        print(f"💡 Submission Calendar: {'Available' if data.get('submissionCalendar') else 'No data'}")
        print("-" * 50)

    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)

if __name__ == "__main__":
    fetch_leetcode_stats()
