from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Predict.html')

scaler = StandardScaler()
@app.route('/',methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Lead_Origin=request.form['lead_Origin']
        if(Lead_Origin=='API'):
            Lead_Origin_API=1
            Lead_Origin_Landing_Page_Submission=0
            Lead_Origin_Lead_Add_Form=0
            Lead_Origin_Lead_Import=0
        elif(Lead_Origin=='Landing_Page_Submission'):
            Lead_Origin_API=0
            Lead_Origin_Landing_Page_Submission=1
            Lead_Origin_Lead_Add_Form=0
            Lead_Origin_Lead_Import=0
        elif(Lead_Origin=='Lead_Add_Form'):
            Lead_Origin_API=0
            Lead_Origin_Landing_Page_Submission=0
            Lead_Origin_Lead_Add_Form=1
            Lead_Origin_Lead_Import=0
        elif(Lead_Origin=='Lead_Import'):
            Lead_Origin_API=0
            Lead_Origin_Landing_Page_Submission=0
            Lead_Origin_Lead_Add_Form=0
            Lead_Origin_Lead_Import=1
        else:
            Lead_Origin_API=0
            Lead_Origin_Landing_Page_Submission=0
            Lead_Origin_Lead_Add_Form=0
            Lead_Origin_Lead_Import=0

        Lead_Source=request.form['lead_Source']
        if(Lead_Source=='Direct_Traffic'):
            Lead_Source_Direct_Traffic=1
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Facebook'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=1
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Google'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=1
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Olark_Chat'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=1
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Organic_Search'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=1
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Others'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=1
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Reference'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=1
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Referral_Site'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=1
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Social_Media'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=1
            Lead_Source_Welingak_Website=0
        elif(Lead_Source=='Welingak_Website'):
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=1
        else:
            Lead_Source_Direct_Traffic=0
            Lead_Source_Facebook=0
            Lead_Source_Google=0
            Lead_Source_Olark_Chat=0
            Lead_Source_Organic_Search=0
            Lead_Source_Others=0
            Lead_Source_Reference=0
            Lead_Source_Referral_Sites=0
            Lead_Source_Social_Media=0
            Lead_Source_Welingak_Website=0

        do_Not_Email=request.form['do_Not_Email']
        if(do_Not_Email=='No'):
            Do_Not_Email_No=1
            Do_Not_Email_Yes=0
        elif(do_Not_Email=='Yes'):
            Do_Not_Email_No=0
            Do_Not_Email_Yes=1
        else:
            Do_Not_Email_No=0
            Do_Not_Email_Yes=0

        TotalVisits = int(request.form['TotalVisits'])
        
        Total_Time_Spent_on_Website = int(request.form['Total_Time_Spent_on_Website'])

        Page_Views_Per_Visit = float(request.form['Page_Views_Per_Visit'])

        specialization=request.form['specialization']
        if(specialization=='Banking_Investment_And_Insurance'):
            Specialization_Banking_Investment_And_Insurance=1
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Business_Administration'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=1
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='E_Business'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=1
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='E_COMMERCE'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=1
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='International_Business'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=1
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Management_Specializations'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=1
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Media_and_Advertising'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=1
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Not_Specified'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=1
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Rural_and_Agribusiness'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=1
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Services_Excellence'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=1
            Specialization_Travel_and_Tourism=0
        elif(specialization=='Travel_and_Tourism'):
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=1
        else:
            Specialization_Banking_Investment_And_Insurance=0
            Specialization_Business_Administration=0
            Specialization_E_Business=0
            Specialization_E_COMMERCE=0
            Specialization_International_Business=0
            Specialization_Management_Specializations=0
            Specialization_Media_and_Advertising=0
            Specialization_Not_Specified=0
            Specialization_Rural_and_Agribusiness=0
            Specialization_Services_Excellence=0
            Specialization_Travel_and_Tourism=0

        What_is_your_current_Occupation=request.form['What_is_your_current_Occupation']
        if(What_is_your_current_Occupation=='Businessman'):
            What_is_your_current_Occupation_Businessman=1
            What_is_your_current_Occupation_Housewife=0
            What_is_your_current_Occupation_Other=0
            What_is_your_current_Occupation_Student=0
            What_is_your_current_Occupation_Unemployed=0
            What_is_your_current_Occupation_Working_Professional=0
    
        elif(What_is_your_current_Occupation=='Housewife'):
            What_is_your_current_Occupation_Businessman=0
            What_is_your_current_Occupation_Housewife=1
            What_is_your_current_Occupation_Other=0
            What_is_your_current_Occupation_Student=0
            What_is_your_current_Occupation_Unemployed=0
            What_is_your_current_Occupation_Working_Professional=0
    
        elif(What_is_your_current_Occupation=='Other'):
            What_is_your_current_Occupation_Businessman=0
            What_is_your_current_Occupation_Housewife=0
            What_is_your_current_Occupation_Other=1
            What_is_your_current_Occupation_Student=0
            What_is_your_current_Occupation_Unemployed=0
            What_is_your_current_Occupation_Working_Professional=0
    
        elif(What_is_your_current_Occupation=='Student'):
            What_is_your_current_Occupation_Businessman=0
            What_is_your_current_Occupation_Housewife=0
            What_is_your_current_Occupation_Other=0
            What_is_your_current_Occupation_Student=1
            What_is_your_current_Occupation_Unemployed=0
            What_is_your_current_Occupation_Working_Professional=0
    
        elif(What_is_your_current_Occupation=='Unemployed'):
            What_is_your_current_Occupation_Businessman=0
            What_is_your_current_Occupation_Housewife=0
            What_is_your_current_Occupation_Other=0
            What_is_your_current_Occupation_Student=0
            What_is_your_current_Occupation_Unemployed=1
            What_is_your_current_Occupation_Working_Professional=0
    
        elif(What_is_your_current_Occupation=='Working Professional'):
            What_is_your_current_Occupation_Businessman=0
            What_is_your_current_Occupation_Housewife=0
            What_is_your_current_Occupation_Other=0
            What_is_your_current_Occupation_Student=0
            What_is_your_current_Occupation_Unemployed=0
            What_is_your_current_Occupation_Working_Professional=1
    
        else:
            What_is_your_current_Occupation_Businessman=0
            What_is_your_current_Occupation_Housewife=0
            What_is_your_current_Occupation_Other=0
            What_is_your_current_Occupation_Student=0
            What_is_your_current_Occupation_Unemployed=0
            What_is_your_current_Occupation_Working_Professional=0
    
        tags=request.form['tags']
        if(tags=='Closed_by_Horizzon'):
            Tags_Closed_by_Horizzon=1
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0
            
        if(tags=='Busy'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=1
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0            

        elif(tags=='Interested_in_other_courses'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=1
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0
    
        elif(tags=='Lost_to_EINS'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=1
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0
    
        elif(tags=='Not_Specified'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=1
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0
    
        elif(tags=='Other_Tags'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=1
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0
    
        elif(tags=='Ringing'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=1
            Tags_Will_revert_after_reading_the_email=0
    
        elif(tags=='Will_revert_after_reading_the_email'):
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=1
    
        else:
            Tags_Closed_by_Horizzon=0
            Tags_Busy=0
            Tags_Interested_in_other_courses=0
            Tags_Lost_to_EINS=0
            Tags_Not_Specified=0
            Tags_Other_Tags=0
            Tags_Ringing=0
            Tags_Will_revert_after_reading_the_email=0
    
        city=request.form['city']
        if(city=='Mumbai'):
            city_Mumbai=1
            city_Other_Cities=0
            city_Other_Cities_of_Maharashtra=0
            city_Other_Metro_Cities=0
            city_Thane_and_Outskirts=0
            city_Tier_II_Cities=0
    
        elif(city=='Other_Cities'):
            city_Mumbai=0
            city_Other_Cities=1
            city_Other_Cities_of_Maharashtra=0
            city_Other_Metro_Cities=0
            city_Thane_and_Outskirts=0
            city_Tier_II_Cities=0
    
        elif(city=='Other_Cities_of_Maharashtra'):
            city_Mumbai=0
            city_Other_Cities=0
            city_Other_Cities_of_Maharashtra=1
            city_Other_Metro_Cities=0
            city_Thane_and_Outskirts=0
            city_Tier_II_Cities=0
    
        elif(city=='Other_Metro_Cities'):
            city_Mumbai=0
            city_Other_Cities=0
            city_Other_Cities_of_Maharashtra=0
            city_Other_Metro_Cities=1
            city_Thane_and_Outskirts=0
            city_Tier_II_Cities=0
    
        elif(city=='Thane_and_Outskirts'):
            city_Mumbai=0
            city_Other_Cities=0
            city_Other_Cities_of_Maharashtra=0
            city_Other_Metro_Cities=0
            city_Thane_and_Outskirts=1
            city_Tier_II_Cities=0
    
        elif(city=='Tier_II_Cities'):
            city_Mumbai=0
            city_Other_Cities=0
            city_Other_Cities_of_Maharashtra=0
            city_Other_Metro_Cities=0
            city_Thane_and_Outskirts=0
            city_Tier_II_Cities=1
    
        else:
            city_Mumbai=0
            city_Other_Cities=0
            city_Other_Cities_of_Maharashtra=0
            city_Other_Metro_Cities=0
            city_Thane_and_Outskirts=0
            city_Tier_II_Cities=0
    
        A_free_copy_of_Mastering_The_Interview=request.form['A_free_copy_of_Mastering_The_Interview']
        if(A_free_copy_of_Mastering_The_Interview=='Yes'):
            A_free_copy_of_Mastering_The_Interview_Yes=1
            A_free_copy_of_Mastering_The_Interview_No=0
    
        elif(A_free_copy_of_Mastering_The_Interview=='No'):
            A_free_copy_of_Mastering_The_Interview_Yes=0
            A_free_copy_of_Mastering_The_Interview_No=1
    
        else:
            A_free_copy_of_Mastering_The_Interview_Yes=0
            A_free_copy_of_Mastering_The_Interview_No=0
    
        Last_Notable_Activity=request.form['Last_Notable_Activity']
        if(Last_Notable_Activity=='Email_Link_Clicked'):
            Last_Notable_Activity_Email_Link_Clicked=1
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=0
    
        elif(Last_Notable_Activity=='Email_Opened'):
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=1
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=0
    
        elif(Last_Notable_Activity=='Modified'):
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=1
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=0
    
        elif(Last_Notable_Activity=='Olark_Chat_Conversation'):
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=1
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=0
    
        elif(Last_Notable_Activity=='Other_Notable_Activity'):
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=1
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=0
    
        elif(Last_Notable_Activity=='Page_Visited_on_Website'):
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=1
            Last_Notable_Activity_SMS_Sent=0
    
        elif(Last_Notable_Activity=='SMS_Sent'):
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=1
    
        else:
            Last_Notable_Activity_Email_Link_Clicked=0
            Last_Notable_Activity_Email_Opened=0
            Last_Notable_Activity_Modified=0
            Last_Notable_Activity_Olark_Chat_Conversation=0
            Last_Notable_Activity_Other_Notable_activity=0
            Last_Notable_Activity_Page_Visited_on_Website=0
            Last_Notable_Activity_SMS_Sent=0
            
        prediction=model.predict([[Lead_Origin_API, Lead_Origin_Landing_Page_Submission, 
                                   Lead_Origin_Lead_Add_Form, Lead_Origin_Lead_Import,
                                   Lead_Source_Direct_Traffic, Lead_Source_Facebook, Lead_Source_Google, 
                                   Lead_Source_Olark_Chat, Lead_Source_Organic_Search, Lead_Source_Others, 
                                   Lead_Source_Reference, Lead_Source_Referral_Sites, 
                                   Lead_Source_Social_Media, Lead_Source_Welingak_Website, Do_Not_Email_No,
                                   Do_Not_Email_Yes, TotalVisits, Total_Time_Spent_on_Website,
                                   Page_Views_Per_Visit, Specialization_Banking_Investment_And_Insurance, 
                                   Specialization_Business_Administration, Specialization_E_Business,
                                   Specialization_E_COMMERCE, Specialization_International_Business, 
                                   Specialization_Management_Specializations, Specialization_Media_and_Advertising, 
                                   Specialization_Not_Specified, Specialization_Rural_and_Agribusiness, 
                                   Specialization_Services_Excellence, Specialization_Travel_and_Tourism, 
                                   What_is_your_current_Occupation_Businessman, What_is_your_current_Occupation_Housewife, 
                                   What_is_your_current_Occupation_Other, What_is_your_current_Occupation_Student, 
                                   What_is_your_current_Occupation_Unemployed, What_is_your_current_Occupation_Working_Professional, 
                                   Tags_Closed_by_Horizzon, Tags_Busy, Tags_Interested_in_other_courses, 
                                   Tags_Lost_to_EINS, Tags_Not_Specified, Tags_Other_Tags, Tags_Ringing, 
                                   Tags_Will_revert_after_reading_the_email, city_Mumbai, city_Other_Cities, 
                                   city_Other_Cities_of_Maharashtra, city_Other_Metro_Cities, 
                                   city_Thane_and_Outskirts, city_Tier_II_Cities, A_free_copy_of_Mastering_The_Interview_Yes, 
                                   A_free_copy_of_Mastering_The_Interview_No, Last_Notable_Activity_Email_Link_Clicked, 
                                   Last_Notable_Activity_Email_Opened, Last_Notable_Activity_Modified, 
                                   Last_Notable_Activity_Olark_Chat_Conversation, Last_Notable_Activity_Other_Notable_activity, 
                                   Last_Notable_Activity_Page_Visited_on_Website, Last_Notable_Activity_SMS_Sent]])
        output=round(prediction[0],2)
        if output<0.8:
            return render_template('Predict.html',prediction_text="lead cannot be converted")
        else:
            return render_template('Predict.html',prediction_text="Lead can be converted")
    else:
        return render_template('Predict.html')

if __name__=="__main__":
    app.run(debug=True)
