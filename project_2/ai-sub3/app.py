import data
import model as ml
import tensorflow as tf
import sqlite3
import os
import pickle
import numpy as np

from flask import g
from threading import Thread
from configs import DEFINES
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter


# slack 연동 정보 입력 부분
SLACK_TOKEN = "xoxb-731514265045-731533587669-VyjAdoE7GcCwFTKQAnJwkNbr"
SLACK_SIGNING_SECRET = "1b3d481d440dfbce442cd23839225f7e"

app = Flask(__name__)

slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Req. 2-2-1 대답 예측 함수 구현
def predict(channel, text):
    tf.logging.set_verbosity(tf.logging.ERROR)

    char2idx, idx2char, vocabulary_length = data.load_voc()

    predic_input_enc = data.enc_processing([text], char2idx)

    predic_input_dec = data.dec_input_processing([""], char2idx)

    predic_target_dec = data.dec_target_processing([""], char2idx)

    classifier = tf.estimator.Estimator(
        model_fn=ml.Model,
        model_dir=DEFINES.check_point_path,
        params={
            'hidden_size': DEFINES.hidden_size,
            'layer_size': DEFINES.layer_size,
            'learning_rate': DEFINES.learning_rate,
            'vocabulary_length': vocabulary_length,
            'embedding_size': DEFINES.embedding_size,
            'embedding': DEFINES.embedding,
            'multilayer': DEFINES.multilayer,
        })

    for i in range(DEFINES.max_sequence_length):

        if i > 0:

            predic_input_dec = data.dec_input_processing([answer], char2idx)

            predic_target_dec = data.dec_target_processing([answer], char2idx)

        predictions = classifier.predict(input_fn=lambda: data.eval_input_fn(predic_input_enc, predic_input_dec, predic_target_dec, 1))

        answer = data.pred_next_string(predictions, idx2char)

    slack_web_client.chat_postMessage(
        channel=channel,
        text=answer
    )
    
# Req 2-2-2. app.db 를 연동하여 웹에서 주고받는 데이터를 DB로 저장
def db_save(text):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('INSERT INTO search_history(query) VALUES(?)', (text,))
    conn.commit()
    conn.close()
    return

# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    channel = event_data["event"]["channel"]
    text = event_data["event"]["text"]

    text = text.split()
    text.pop(0)
    text = " ".join(text)
    db_save(text)
    t = Thread(target=predict, args=(channel, text))
    t.start()


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run()
