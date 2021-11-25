import vk_api
import Token
import random
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from game_city import Cities
from correct_cities import correct_cities

dif_answer = ["Привет", "Привет, я мега пупер бот, могу ответить на твой вопрос",
              "Привет, я могу тебя заскамить", "Привет, а ты знал, что ты лох!"]
dif_answer2 = ["Нормально, ты как?",
               "Пока не родила",
               "Ты даун, какие дела, сегодня было три физики, я чуть не сдох",
               "Отлично, потому что меня писал прекрасный программист Никита"]

vk_session = vk_api.VkApi(token=Token.TOKEN)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

player_in_game = []
active_game = []


def is_correct_event(event):
    return event.to_me and event.type == VkEventType.MESSAGE_NEW


def send_message(user_id, message):
    vk_session.method("messages.send", {"user_id": user_id,
                                        "message": message,

                                        "random_id": 0})


def is_game(event):
    game_command = ["начали", "сыграем в города", "города"]
    return event.text.lower() in game_command


def kill_game(game):
    user_ids = game.user_ids
    active_game.pop(active_game.index(game))
    player_in_game.remove(user_ids[0])
    player_in_game.remove(user_ids[1])


def main():
    user_in_queue = None
    for event in longpoll.listen():
        if is_correct_event(event):
            if event.text == "Привет" or event.text == "привет":
                send_message(event.user_id, dif_answer[random.randint(0, len(dif_answer) - 1)])
            elif event.text == "Как дела" or event.text == "Как дела?" or event.text == "как дела?" or event.text == "как дела":
                send_message(event.user_id, dif_answer2[random.randint(0, len(dif_answer) - 1)])
            elif event.text == "secret_comand":
                send_message(event.user_id, "я гениальное твоерение Мокийчука Никиты Артуровича")
            elif is_game(event):
                if user_in_queue is None:
                    send_message(event.user_id, " Вы встали в очередь на игру в города")
                    user_in_queue = event.user_id
                elif event.user_id != user_in_queue:
                    send_message(user_in_queue, "Мы нашли вам оппонента")
                    send_message(event.user_id, "Оппонент уже ожидает вас")
                    active_game.append(Cities(user_in_queue, event.user_id))
                    player_in_game.append(user_in_queue)
                    player_in_game.append(event.user_id)
                    first_user = active_game[-1].user_ids[active_game[-1].current_step]
                    send_message(first_user, "Вы ходите первым! Назовите город на любую букву.")
                    user_in_queue = None
            elif event.user_id in player_in_game:
                bad = False
                igra = ""
                for game in active_game:
                    if event.user_id in game.user_ids:
                        if game.user_ids.index(event.user_id) != game.current_step:
                            bad = True
                            break
                        else:
                            igra = game
                if bad:
                    send_message(event.user_id, "Сейчас не ваш ход!")
                    continue
                user1 = event.user_id
                user2 = igra.user_ids[1 - igra.current_step]
                if not igra.is_correct_first_char(event.text[0].upper()):
                    send_message(igra.user_ids[1 - igra.current_step], "Вы победили")
                    send_message(event.user_id, "Вы назвали город не на ту букву и вы проиграли")
                    kill_game(igra)
                    continue
                city = event.text.capitalize()
                if city not in correct_cities:
                    send_message(user1, "Такого города нет в нашем списке городов!")
                    send_message(user2, "Вы победили!")
                    kill_game(igra)
                    continue
                if  igra.is_unused_city(city):
                    send_message(user1, " Такой город уже называли. Увы, вы проиграли")
                    send_message(user2, " Вы победили")
                    kill_game(igra)
                    continue
                igra.used_cities.append(city)
                igra.change_last_char(city)
                igra.current_step = 1 - igra.current_step
                send_message(user2, "Ваш ход! Оппонент назвал город:" + city + ".\nВам на букву: " + igra.last_char)
            else:
                send_message(event.user_id, "Я пока знаю, только команды привет и как дела")


main()
