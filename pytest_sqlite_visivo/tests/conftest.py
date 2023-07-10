import sqlite3
import pytest 

def pytest_sessionfinish(session):
    # Connect to the SQLite database
    conn = sqlite3.connect('../pytestResults.db')
    cursor = conn.cursor()

    # Get the test results from the pytest session object
    print(dir(session.config.hook))
    results = session.config.hook.pytest_collectreport(
        report=pytest.Report(tests=session.testscollected)
    )

    # Loop through the test results and insert them into the database
    for result in results:
        # Extract the relevant information from the result object
        test_name = result.nodeid
        outcome = result.outcome
        duration = result.duration

        # Insert the test result into the database
        cursor.execute("INSERT INTO test_results (test_name, outcome, duration) VALUES (?, ?, ?)",
                       (test_name, outcome, duration))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
