# Chinese Zodiac Sign Program

## Requirements
- Ask the user to input their birth year.
- Determine and display the corresponding Chinese Zodiac sign based on the birth year, using the 12-year cycle:
  i. Rat (鼠 / Shǔ)
  ii. Ox (牛 / Niú)
  iii. Tiger (虎 / Hǔ)
  iv. Rabbit (兔 / Tù)
  v. Dragon (龙 / Lóng)
  vi. Snake (蛇 / Shé)
  vii. Horse (马 / Mǎ)
  viii. Goat (羊 / Yáng)
  ix. Monkey (猴 / Hóu)
  x. Rooster (鸡 / Jī)
  xi. Dog (狗 / Gǒu)
  xii. Pig (猪 / Zhū)

## Code
```python
zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)",
          "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)",
          "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

user_birth_year = int(input("Input Birth Year: "))
print(f"Your Chinese Zodiac Sign is: {zodiac[user_birth_year % 12]}")
```

## Output
![Program Output](zodiac_screenshot.png)
