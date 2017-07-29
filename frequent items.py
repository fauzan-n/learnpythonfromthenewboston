from collections import Counter

text ="Autonomous cars often proudly claim to be fitted with " \
      "a long list of sensors—cameras, ultrasound, radar, lidar, " \
      "you name it. But if you’ve ever wondered why so many " \
      "sensors are required, look no further than this picture." \
      "You’re looking at what’s known in the autonomous-car industry " \
      "as an “edge case”—a situation where a vehicle might have " \
      "behaved unpredictably because its software processed " \
      "an unusual scenario differently from the way a human would."

words = text.split()
counter = Counter(words)
top_three = counter.most_common(4);print(top_three)
