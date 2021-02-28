from selenium import webdriver
import os
import sys

contest_number = str(sys.argv[1])

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://codeforces.com/contest/" + contest_number)

q = driver.find_element_by_class_name("problems")
a = q.find_elements_by_tag_name("tr")
problem_list = []

for y in range(len(a)):
    if y == 0:
        continue
    b = a[y].find_elements_by_tag_name("td")
    problem_list.append(b[0].find_element_by_tag_name("a").get_attribute("href"))

address = os.getcwd()

os.mkdir(contest_number)
for x in range(0, len(problem_list)):
    driver.get(problem_list[x])
    info = problem_list[x].split("/")
    location = address + "/" + contest_number + "/" + info[-1]
    os.mkdir(location)
    S = lambda X: driver.execute_script("return document.body.parentNode.scroll" + X)
    driver.set_window_size(S("Width"), S("Height"))
    ss = driver.find_element_by_class_name("problem-statement").screenshot(location + "/problem.png")

    input_list = driver.find_elements_by_class_name("input")
    output_list = driver.find_elements_by_class_name("output")

    for i in range(len(input_list)):
        details1 = input_list[i].text
        f1 = open(location + "/input" + str(i + 1) + ".txt", "w")
        count1 = 0
        for element1 in details1:
            if element1 == "\n":
                count1 += 1
            if count1 > 1:
                f1.write(element1)

        f1.close()

        details2 = output_list[i].text
        f2 = open(location + "/output" + str(i + 1) + ".txt", "w")
        count2 = 0
        for element2 in details2:
            if element2 == "\n":
                count2 += 1
            if count2 > 1:
                f2.write(element2)

        f2.close()

driver.quit()
