from datetime import datetime, timedelta

from flask import Flask, request, session, make_response
import requests
from twilio.twiml.messaging_response import MessagingResponse
SECRET_KEY = 'pk4AXNoQCJe4RKTNyHzmuDPxaUmYx'
app = Flask(__name__)
app.secret_key = SECRET_KEY




@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    counter = session.get('counter', 0)
    state = str(request.cookies.get('state', 'start'))
    print(counter)
    print(state)
    print('Previous menu: ' + state)

    session['counter'] = counter

    counter += 1
    previousMessage = str(request.cookies.get('state', ''))

    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    ########################################################################
    if incoming_msg == '00' or 'hello' in incoming_msg:
        welocme_msg = ("Hello! I'm your Openserve virtual assitant. How can I help you?\n")
        NeedHelp = ("[1] I need help\n")
        GetConnected = ("[2] I want to get connected\n")
        Info = ("[3] I need info\n")
        App = ("[4] Download App\n")
        datalist = welocme_msg + NeedHelp + GetConnected + Info + App
        msg.body(datalist)

        message=datalist
        twml = MessagingResponse()
        twml.message(message)

        expires = datetime.utcnow() + timedelta(hours=4)
        resp = make_response(str(twml))
        resp.set_cookie('state', value='menuMain', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
        print(state)
        counter = session.get('counter', 1)

        print(counter)
        return resp
    elif state=='menuMain':
        if incoming_msg == '1':
            hear_you = ("I hear you, let's take a look at what I can help you with:\n")
            installation = ("[1] Setup and Installation\n")
            support = ("[2] Need support - who to contact.\n")
            coverage = ("[3] Coverage and application\n")
            service_number = ("[4] I need my Service / B-Number\n")
            network_speed = ("[5] Network speed and connectivity matters\n")
            datalist2 = hear_you + installation + support + coverage + service_number + network_speed
            msg.body(datalist2)

            message = datalist2
            twml = MessagingResponse()
            twml.message(message)

            expires = datetime.utcnow() + timedelta(hours=4)
            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueHelp', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '2':
            sure_thing = ("Sure thing! What would you like to get connected?\n")
            connect_home = ("[1] Connect my home \n")
            connect_bussiness = ("[2] Connect my business \n")
            connect_estate = ("[3]Connect my estate \n")
            connect_customers = ("[4] Connect my customers \n")
            expires = datetime.utcnow() + timedelta(hours=4)

            datalist3 = sure_thing + connect_home + connect_bussiness + connect_estate + connect_customers
            msg.body(datalist3)
            message = datalist3
            twml = MessagingResponse()
            twml.message(message)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp

###########################################################################

    if state=='menueHelp':
        if incoming_msg == '1':
            sure_thing = ("I here you, lets take a look at what I can help you with:\n")
            B_Number=("[1] I need my Service / B-Number \n")
            Network_Speed=("[2] Network Speed and connectivity matters \n")
            Setup=("[3] Setup and installation \n")
            Support=("[4] Need Support - who to contact \n")
            Coverage=("[5] Coverage and application \n")

            datalist1_1 = sure_thing+B_Number+Network_Speed+Setup+Support+Coverage
            msg.body(datalist1_1)
            message = datalist1_1
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_B', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
    if state=='menueConnect':
        if incoming_msg == '1':
            connect_H_msg=("OK, so you want to get your home connected? Here's how to get started:\n")
            check_coverage=("[1] Check if my area is covered \n")
            best_speed=("[2] Find out what speed is best for me\n")
            Browse_ISP=("[3] Browse ISP Deals\n")
            Fibre_info=("[4] Tell me more about Fibre\n")
            datalist1_connect_menu=connect_H_msg+check_coverage+best_speed+Browse_ISP+Fibre_info
            msg.body(datalist1_connect_menu)
            message = datalist1_connect_menu
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Home', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '2':
            connect_B_msg=("I see you've selected to connect your business. What would you like to do first? \n")
            coverage_map=("[1] Show me the Fibre coverage map \n")
            speed=("[2] Determine what speed suits my needs \n")
            ISP_Plans=("[3] Let me see ISP Plans and Deals \n")
            Fibre_Info=("[4] Learn more about Fibre \n")

            datalist2_connect_menu=connect_B_msg+coverage_map+speed+ISP_Plans+Fibre_Info

            msg.body(datalist2_connect_menu)
            message = datalist2_connect_menu
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Business', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '3':
            estate_msg=("Excellent - here's what you need: \n")
            msg.body(estate_msg)
            message = estate_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Estate', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '4':
            customer_msg = ("Sure, would you like some instant info on one of these product options, or should I get someone to call you? \n")
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Customers', expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
    if state == 'menueConnect_Business':
        if incoming_msg == '1':
            excellent_msg = ("Excellent, here's what you need")
            customer_msg = excellent_msg
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Business_B',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '2':
            perfect_msg = ("Perfect, here you go.")
            customer_msg = perfect_msg
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Business_B',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '3':
            perfect_msg = ("Perfect, here you go.")
            customer_msg = perfect_msg
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Business_B',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '4':
            sure_msg = ("Sure thing , here you are.")
            customer_msg = sure_msg
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Business_B',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '5':
            no_prob_msg = ("Not a problem, here's what you need.")
            customer_msg = no_prob_msg
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Business_B',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp



    if state == 'menueConnect_Home':
        if incoming_msg == '1':
            got_it = ("Got it! Here you go!")
            customer_msg=got_it
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Customers',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '2':
            no_problem = ("No Problem. Here's what you need.")
            customer_msg = no_problem
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Customers',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '3':
            great_covered = ("Great! I've got you covered. Here you go")
            customer_msg = great_covered
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Customers',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp
        elif incoming_msg == '4':
            try_this=("Sure thing, try this.")
            customer_msg = try_this
            msg.body(customer_msg)
            message = customer_msg
            twml = MessagingResponse()
            twml.message(message)
            expires = datetime.utcnow() + timedelta(hours=4)

            resp = make_response(str(twml))
            resp.set_cookie('state', value='menueConnect_Customers',
                            expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))
            print(state)
            return resp

    if incoming_msg == '2.1.1':
        got_it=("Got it! Here you go!")

        datalist2_1_1=got_it
        msg.body(datalist2_1_1)
        responded=True

    if incoming_msg == '2.1.2':
        no_problem=("No Problem. Here's what you need.")

        datalist2_1_2 = no_problem
        msg.body(datalist2_1_2)
        responded = True

    if incoming_msg == '2.1.3':
        great_covered=("Great! I've got you covered. Here you go")

        datalist2_1_3 = great_covered
        msg.body(datalist2_1_3)
        responded=True
    if incoming_msg == '2.1.4':
        tell_me_more=("Tell me more about Fibre")

        datalist2_1_4 = tell_me_more
        msg.body(datalist2_1_4)
        responded=True

    if incoming_msg == '3':
        sure_thing_info=("Sure thing! What would you like information on? \n")
        broadband=("[3.1] Perfect! We have a few Broadband products and services. Have a look at them here.\n")
        data_internet=("[3.2]Sure thing! We have a few Data/Internet products and services. Here\n")
        Managed_Services=("[3.3]Not a problem. We have a few Managed Service offerings. Here\n")
        Voice=("[3.4] Great, I've got you covered. We have a couple of Voice offerings. Here \n")
        other=("[3.5] Lets make sure you get that information you need")

        datalist4=sure_thing_info+broadband+data_internet+Managed_Services+Voice+other
        msg.body(datalist4)
        responded = True

    if 'hi' in incoming_msg:
        welocme_msg=("Hello! I'm your Openserve virtual assitant. How can I help you?\n")
        NeedHelp=("[1] I need help\n")
        GetConnected=("[2] I want to get connected\n")
        Info=("[3] I need info\n")
        App=("[4] Download App\n")

        datalist = welocme_msg + NeedHelp + GetConnected + Info + App
        msg.body(datalist)
        responded = True

    # if incoming_msg == '2':
    #     sure_thing=("Sure thing! What would you like to get connected?\n")
    #     connect_home=("[2.1] Connect my home \n")
    #     connect_bussiness=("[2.2] Connect my business \n")
    #     connect_estate=("[2.3]Connect my estate \n")
    #     connect_customers=("[2.4] Connect my customers \n")
    #
    #     datalist3=sure_thing+connect_home+connect_bussiness+connect_estate+connect_customers
    #     msg.body(datalist3)
    #     responded = True


    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run(port=5000)