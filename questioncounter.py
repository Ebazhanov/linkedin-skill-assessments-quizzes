# To run this file:
# 1. install python
# 2. download the linkedin-skill-assessments-quizzes github
# 3. in a terminal running from that folder, run `python questioncounter.py`

import os
# this will count all the questions as long as the .md files do not have any curly quotations or dog emojis 🐶 (
# css-line 1855)
# simply run the script in python and it will print out all of the files, first listing "total questions" followed by
# [x] "answered questions, then [ ] unanswered questions.
# install python, then open a python terminal, then run the python script and read the output. This script does not
# automatically update the main README.MD file, so any changes will have to be done manually, or someone else can
# write a script to automatically update each of the values.

with os.scandir('./') as entries:
    for entry in entries:
        if entry.is_dir() and not entry.name.startswith('.') and not entry.name.startswith('assets') and not \
                entry.name.startswith('venv'):
            filename = entry.path + entry.path[1:] + '-quiz.md'
            # print(filename)
            with open(filename) as f:
                text = f.read()
                answered = text.count("[x]")  # counts correct answers, very accurate
                unanswered = (text.count("[ ]") - 3 * answered)/4  # counts total answers, tries to keep track of
                # unanswered questions, but because some people only leave the correct answer, this will not always
                # be correct
                total = answered + unanswered  # totals the questions we think there are
                print(f"{filename} {total} [x] {answered} [ ] {unanswered}")


# Results 10/18/2022
# ./accounting/accounting-quiz.md 74.0 [x] 52 [ ] 22.0
# ./adobe-acrobat/adobe-acrobat-quiz.md 27.0 [x] 22 [ ] 5.0
# ./adobe-illustrator/adobe-illustrator-quiz.md 77.0 [x] 75 [ ] 2.0
# ./adobe-in-design/adobe-in-design-quiz.md 42.0 [x] 40 [ ] 2.0
# ./adobe-lightroom/adobe-lightroom-quiz.md 20.0 [x] 20 [ ] 0.0
# ./adobe-photoshop/adobe-photoshop-quiz.md 97.25 [x] 94 [ ] 3.25
# ./adobe-premiere-pro/adobe-premiere-pro-quiz.md 48.0 [x] 36 [ ] 12.0
# ./adobe-xd/adobe-xd-quiz.md 21.0 [x] 18 [ ] 3.0
# ./after-effects/after-effects-quiz.md 24.25 [x] 13 [ ] 11.25
# ./agile-methodologies/agile-methodologies-quiz.md 121.0 [x] 121 [ ] 0.0
# ./android/android-quiz.md 71.0 [x] 72 [ ] -1.0
# ./angular/angular-quiz.md 66.0 [x] 65 [ ] 1.0
# ./arc-gis/arc-gis-quiz.md 5.0 [x] 5 [ ] 0.0
# ./autocad/autocad-quiz.md 76.75 [x] 75 [ ] 1.75
# ./autodesk-fusion-360/autodesk-fusion-360-quiz.md 37.25 [x] 25 [ ] 12.25
# ./aws/aws-quiz.md 103.5 [x] 104 [ ] -0.5
# ./aws-lambda/aws-lambda-quiz.md 57.0 [x] 55 [ ] 2.0
# ./bash/bash-quiz.md 78.0 [x] 77 [ ] 1.0
# ./c++/c++-quiz.md 91.0 [x] 90 [ ] 1.0
# ./c-(programming-language)/c-(programming-language)-quiz.md 79.0 [x] 79 [ ] 0.0
# ./c-sharp/c-sharp-quiz.md 73.0 [x] 73 [ ] 0.0
# ./css/css-quiz.md 158.25 [x] 159 [ ] -0.75
# ./cybersecurity/cybersecurity-quiz.md 122.75 [x] 127 [ ] -4.25
# ./django/django-quiz.md 76.0 [x] 76 [ ] 0.0
# ./dotnet-framework/dotnet-framework-quiz.md 71.25 [x] 72 [ ] -0.75
# ./eclipse/eclipse-quiz.md 43.0 [x] 36 [ ] 7.0
# ./front-end-development/front-end-development-quiz.md 85.0 [x] 85 [ ] 0.0
# ./git/git-quiz.md 135.0 [x] 135 [ ] 0.0
# ./go/go-quiz.md 45.0 [x] 45 [ ] 0.0
# ./google-ads/google-ads-quiz.md 50.0 [x] 50 [ ] 0.0
# ./google-analytics/google-analytics-quiz.md 86.0 [x] 85 [ ] 1.0
# ./google-cloud-platform/google-cloud-platform-quiz.md 66.0 [x] 66 [ ] 0.0
# ./hadoop/hadoop-quiz.md 68.75 [x] 61 [ ] 7.75
# ./html/html-quiz.md 111.5 [x] 112 [ ] -0.5
# ./it-operations/it-operations-quiz.md 69.0 [x] 69 [ ] 0.0
# ./java/java-quiz.md 154.0 [x] 154 [ ] 0.0
# ./javascript/javascript-quiz.md 141.0 [x] 142 [ ] -1.0
# ./jquery/jquery-quiz.md 81.0 [x] 79 [ ] 2.0
# ./json/json-quiz.md 87.25 [x] 87 [ ] 0.25
# ./keynote/keynote-quiz.md 14.0 [x] 0 [ ] 14.0
# ./kotlin/kotlin-quiz.md 88.0 [x] 89 [ ] -1.0
# ./linux/linux-quiz.md 101.25 [x] 100 [ ] 1.25
# ./logic-pro/logic-pro-quiz.md 17.0 [x] 17 [ ] 0.0
# ./machine-learning/machine-learning-quiz.md 105.75 [x] 106 [ ] -0.25
# ./matlab/matlab-quiz.md 71.0 [x] 72 [ ] -1.0
# ./maven/maven-quiz.md 68.0 [x] 65 [ ] 3.0
# ./microsoft-access/microsoft-access-quiz.md 30.0 [x] 30 [ ] 0.0
# ./microsoft-azure/microsoft-azure-quiz.md 60.0 [x] 60 [ ] 0.0
# ./microsoft-excel/microsoft-excel-quiz.md 147.0 [x] 148 [ ] -1.0
# ./microsoft-outlook/microsoft-outlook-quiz.md 93.25 [x] 72 [ ] 21.25
# ./microsoft-power-automate/microsoft-power-automate-quiz.md 26.25 [x] 25 [ ] 1.25
# ./microsoft-power-bi/microsoft-power-bi-quiz.md 85.0 [x] 84 [ ] 1.0
# ./microsoft-power-point/microsoft-power-point-quiz.md 99.0 [x] 99 [ ] 0.0
# ./microsoft-project/microsoft-project-quiz.md 45.0 [x] 44 [ ] 1.0
# ./microsoft-word/microsoft-word-quiz.md 97.0 [x] 97 [ ] 0.0
# ./mongodb/mongodb-quiz.md 84.0 [x] 86 [ ] -2.0
# ./mysql/mysql-quiz.md 114.0 [x] 113 [ ] 1.0
# ./node.js/node.js-quiz.md 80.0 [x] 76 [ ] 4.0
# ./nosql/nosql-quiz.md 48.0 [x] 47 [ ] 1.0
# ./object-oriented-programming/object-oriented-programming-quiz.md 95.5 [x] 96 [ ] -0.5
# ./objective-c/objective-c-quiz.md 41.0 [x] 39 [ ] 2.0
# ./php/php-quiz.md 98.25 [x] 101 [ ] -2.75
# ./pro-tools/pro-tools-quiz.md 16.0 [x] 2 [ ] 14.0
# ./python/python-quiz.md 162.25 [x] 164 [ ] -1.75
# ./quickbooks/quickbooks-quiz.md 66.0 [x] 39 [ ] 27.0
# ./r/r-quiz.md 54.75 [x] 54 [ ] 0.75
# ./reactjs/reactjs-quiz.md 109.0 [x] 109 [ ] 0.0
# ./rest-api/rest-api-quiz.md 68.0 [x] 68 [ ] 0.0
# ./revit/revit-quiz.md 14.0 [x] 14 [ ] 0.0
# ./ruby-on-rails/ruby-on-rails-quiz.md 75.75 [x] 71 [ ] 4.75
# ./rust/rust-quiz.md 42.0 [x] 42 [ ] 0.0
# ./scala/scala-quiz.md 50.0 [x] 47 [ ] 3.0
# ./search-engine-optimization/search-engine-optimization-quiz.md 76.0 [x] 75 [ ] 1.0
# ./sharepoint/sharepoint-quiz.md 55.0 [x] 38 [ ] 17.0
# ./sketchup/sketchup-quiz.md 2.0 [x] 2 [ ] 0.0
# ./solidworks/solidworks-quiz.md 57.0 [x] 57 [ ] 0.0
# ./spring-framework/spring-framework-quiz.md 84.75 [x] 75 [ ] 9.75
# ./swift/swift-quiz.md 69.25 [x] 70 [ ] -0.75
# ./t-sql/t-sql-quiz.md 50.25 [x] 50 [ ] 0.25
# ./unity/unity-quiz.md 52.0 [x] 50 [ ] 2.0
# ./vba/vba-quiz.md 58.5 [x] 48 [ ] 10.5
# ./visio/visio-quiz.md 41.0 [x] 41 [ ] 0.0
# ./windows-server/windows-server-quiz.md 71.0 [x] 74 [ ] -3.0
# ./wordpress/wordpress-quiz.md 80.0 [x] 79 [ ] 1.0
# ./xml/xml-quiz.md 47.0 [x] 46 [ ] 1.0