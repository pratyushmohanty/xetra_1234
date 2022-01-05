"""Running the Xetra ETL application"""
import logging
import logging.config

import yaml

def main():
    """
        entry point to run the xetra ETL job.
    """
    # Parsing YAML file
    config_path = 'C:/Users/pmohant/source/repos/_Learning/source/repos/UdemyETLPython/xetra_project/xetra_1234/configs/xetra_report1_config.yaml'
    config = yaml.safe_load(open(config_path))
    
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    

if __name__ == '__main__':
    main()