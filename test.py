# x = 20
# x //= 11
# print(x)


# yêu cầu người dùng nhập chiều cao
# nếu chiều cao nhỏ hơn 100 thì miễn phí
# nếu chiều cao từ 100 đến 140 thì 120 nghìn
# nếu chiều cao hơn 140 thì giá vé 200 nghìn


# nhập năm sinh
# nếu nhỏ hơn 18 tuổi hoặc lớn hơn 56 tuổi thì không phải làm gì hết
# còn không thì phải đi làm




# height = float(input('Type your height(cm)? '))
# if height < 100:
#     print('Ticket is free')
# elif height >=100 and height <=140:
#     print('Ticket price is 120.000 dong')
# else:
#     print('Ticket price is 200.000 dong')



# yearOfBirth = int(input('Type your year of birth '))
# age = 2021 - yearOfBirth
# print(age)
# if age <18 or age >56:
#     print('Do nothing')
# else:
#     print('Must to work')


# nhập điểm 6 môn học toán, lí, hoá, sinh, văn, av
# kiểm tra xếp loại giỏi, khá, tb, yếu






markMath = float(input('Type your mark of Math: '))
mare = float(input('Type your mark of Literature: '))
markHistory = float(input('Type your mark of History: '))
markGeography = float(input('Type your mark of Geography: '))
markEnglish = float(input('Type your mark of English: '))
markCivicEducation = float(input('Type your mark of Civic Education: '))
markTechnology = float(input('Type your mark of Technology: '))
markNationalDefenseEducation = float(input('Type your mark of National Defense Education: '))
markAverage = (markMath + markPhysics + markChemistry + markBiology + markInformatics + markLiterature + markHistory + markGeography + markEnglish + markCivicEducation + markTechnology + markNationalDefenseEducation) / 12
if (markMath >=8.0 or markLiterature >=8.0 or markEnglish >=8.0) and markPhysics >=6.5 and markChemistry >=6.5 and markBiology >=6.5 and markInformatics >=6.5 and markHistory >=6.5 and markGeography >=6.5 and markCivicEducation >=6.5 and markTechnology >=6.5 and markNationalDefenseEducation >=6.5 and markAverage >=8.0:
    print('You are the very good student')
elif (markMath >=6.5 or markLiterature >=6.5 or markEnglish >=6.5) and markPhysics >=5.0 and markChemistry >=5.0 and markBiology >=5.0 and markInformatics >=5.0 and markHistory >5.0 and markGeography >=5.0 and markCivicEducation >=5.0 and markTechnology >=5.0 and markNationalDefenseEducation >=5.0 and markAverage >=6.5:
    print('You are the good student')
elif markMath >=5.0 and markPhysics >=5.0 and markChemistry >=5.0 and markBiology >=5.0 and markInformatics >=5.0 and markLiterature >=5.0 and markHistory >=5.0 and markGeography >=5.0 and markEnglish >=5.0 and markCivicEducation >=5.0 and markTechnology >=5.0 and markNationalDefenseEducation >=5.0 and markAverage >=5.0:
    print('You are the average student')
else:
    print('You are fail')




# yêu cầu người dùng nhập dãy ký tự
# Đếm bao nhiêu từ trongdãy ký tự
# xuất từng chữ ra màn hình



# string = input('Type annything: ')
# for x in string:
#     print(x)
























