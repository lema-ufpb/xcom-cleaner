# -*- coding: UTF-8 -*-
"""Import modules"""
from datetime import datetime, timedelta, timezone
from airflow.models import XCom
from airflow.utils.db import provide_session
from airflow.utils.log.logging_mixin import LoggingMixin as task_logger


@provide_session
def cleanup_xcom(session=None, **context):
    """ Clean up xcom  """

    log = task_logger().log
    log.info(f"Initialize {context['ti']}")
    threshold = context["params"]["days"]

    ts_limit = datetime.now(timezone.utc) - timedelta(days=threshold)
    log.info(f"Remove all XCOMs older than {ts_limit}")
    session.query(XCom).filter(
        XCom.execution_date <= ts_limit).delete(
        synchronize_session='fetch')

    return "Task ran successfully!"
