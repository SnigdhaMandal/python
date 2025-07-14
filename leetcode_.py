import requests

def fetch_leetcode_stats(NevroHelios):
    url = f"https://leetcode-stats-api.herokuapp.com/{NevroHelios}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch data for user '{NevroHelios}'. Status code: {response.status_code}")
        return

    data = response.json()

    if 'message' in data:
        print(f"⚠️  Error: {data['message']}")
        return

    print(f"\n📊 LeetCode Stats for @{NevroHelios}\n")
    print(f"✅ Total Solved     : {data['totalSolved']} / {data['totalQuestions']}")
    print(f"📘 Easy            : {data['easySolved']} / {data['totalEasy']}")
    print(f"📙 Medium          : {data['mediumSolved']} / {data['totalMedium']}")
    print(f"📕 Hard            : {data['hardSolved']} / {data['totalHard']}")
    print(f"📈 Acceptance Rate : {data['acceptanceRate']}%")
    print(f"🏆 Ranking         : {data['ranking']}")
    print(f"🎯 Contribution Points: {data['contributionPoints']}")
    print(f"🧠 Reputation      : {data['reputation']}")
    print(f"💡 Submission Calendar: {'Available' if data['submissionCalendar'] else 'No data'}")
    print("-" * 50)

if __name__ == "__main__":
   NevroHelios = input("Enter LeetCode username: ")
    fetch_leetcode_stats(NevroHelios)
