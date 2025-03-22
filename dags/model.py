# -*- coding: UTF-8 -*-
"""Import modules"""
from os.path import abspath, dirname, join
from sys import path as sys_path
from pathlib import Path
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.models.param import Param
from airflow.operators.python import PythonOperator


# initialize airflow base dir
BASE_DIR = dirname(abspath(__file__))
sys_path.append(BASE_DIR)


class DAGModel():
    """
    Create a DAG model for reuse on dag factories projects
    """

    def __init__(self):
        """Handle version"""
        try:
            with open(join(BASE_DIR, '.release')) as f:
                version = f.readline()
            f.close()
        except:
            version = "dev"
        self.version = version

    def __load_docs(self, filename: str) -> str:
        """Load docs from markdown files"""
        return Path(dirname(__file__), filename).read_text(encoding="utf8")

    def create_dag(self, **params):
        """Create model artifact for dag factory"""

        default_args = {
            "owner": params.get('owner'),
            "depends_on_past": False,
            "start_date": datetime(2022, 1, 8),
            'email_on_failure': False,
            "retries": 0,
            "retry_delay": timedelta(minutes=1),
            "dagrun_timeout": timedelta(minutes=params.get('timeout')),
            "on_success_callback": params.get('on_success_callback'),
            "on_failure_callback": params.get('on_failure_callback')
        }

        dag = DAG(
            dag_id=params.get('dag_id'),
            description=params.get('description'),
            default_args=default_args,
            schedule_interval=params.get('schedule'),
            catchup=False,
            tags=params.get('tags'),
            params={
                "days": Param(
                    default=2,
                    type="integer",
                    description="Delete older than days",
                )
            },

        )
        with dag:

            from lib_cleaner_xcom.cleaner import cleanup_xcom

            # Define tasks
            task_1 = PythonOperator(
                task_id="delete-old-xcoms",
                python_callable=cleanup_xcom,
                provide_context=True
            )

            # Model workflow
            task_1

            # Load docs
            dag.doc_md = self.__load_docs("docs/main.md")

        return dag
