from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="localhost",
    database="intern_assessment",
    user="quiz_admin",
    password="SecretPassword123"
)

@app.route('/submit_assessment', methods=['POST'])
def submit_assessment():

    try:
        data = request.json

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO assessment_results (
                phone_number,
                user_id,
                q1,
                q2,
                q3,
                q4,
                q5,
                q6,
                q7,
                q8,
                q9,
                q10,
                compliance_percentage,
                remarks
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s
            )
            ON CONFLICT (user_id)
            DO UPDATE SET
                q1 = EXCLUDED.q1,
                q2 = EXCLUDED.q2,
                q3 = EXCLUDED.q3,
                q4 = EXCLUDED.q4,
                q5 = EXCLUDED.q5,
                q6 = EXCLUDED.q6,
                q7 = EXCLUDED.q7,
                q8 = EXCLUDED.q8,
                q9 = EXCLUDED.q9,
                q10 = EXCLUDED.q10,
                compliance_percentage = EXCLUDED.compliance_percentage,
                remarks = EXCLUDED.remarks,
                submitted_at = CURRENT_TIMESTAMP
        """, (
            data['phone_number'],
            data['user_id'],
            data['q1'],
            data['q2'],
            data['q3'],
            data['q4'],
            data['q5'],
            data['q6'],
            data['q7'],
            data['q8'],
            data['q9'],
            data['q10'],
            data['compliance_percentage'],
            data['remarks']
        ))

        conn.commit()

        cur.close()

        return jsonify({
            "success": True,
            "message": "Assessment saved successfully"
        })

    except Exception as e:

        conn.rollback()
        print("\n====================")
        print("ERROR:")
        print(e)
        print("====================\n")

        return jsonify({
        "success": False,
        "error": str(e)
    }), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)