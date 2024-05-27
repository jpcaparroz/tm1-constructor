from TM1py import TM1Service

def write_database_parameters_in_sys_cube(tm1_service: TM1Service, language: str):
    """Write basic parameters information on system cube (SYS_Parameter)

    Args:
        tm1_service (TM1Service): tm1 service
        language (str): database language parameter (en/pt)
    """

    tm1_service.cells.write_values(
        cellset_as_dict={("parameter", "language"): language},
        cube_name="SYS_Parameter",
        dimensions=["03_Parameter", "01_SYS_Parameter"],
    )

def write_process_info_in_sys_cube(
    tm1_service: TM1Service,
    status_sucessfully_message: str,
    status_error_message: str,
    status_time_format: str,
):
    """Write process information on system cube (SYS_Parameter)

    Args:
        tm1_service (TM1Service): tm1 service
        status_sucessfully_message (str): sucessfully process message
        status_error_message (str): error process message
        status_time_format (str): format date/hour process status
    """

    tm1_service.cells.write_values(
        cellset_as_dict={
            ("parameter", "status_sucessfully_message"): status_sucessfully_message,
            ("parameter", "status_error_message"): status_error_message,
            ("parameter", "status_time_format"): status_time_format,
        },
        cube_name="SYS_Parameter",
        dimensions=["03_Parameter", "01_SYS_Parameter"],
    )

def write_dir_parameters_in_sys_cube(
    tm1_service: TM1Service,
    dir_database: str,
    dir_log: str,
    dir_modelupload: str,
    dir_dq: str,
    dir_sftpin: str,
    dir_sftpout: str,
):
    """Write directory information on system cube (SYS_Parameter)

    Args:
        tm1_service (TM1Service): tm1 service
        dir_database (str): database folder directory
        dir_log (str): log folder directory
        dir_modelupload (str): mode_upload folder directory
        dir_dq (str): dq exe directory
        dir_sftpin (str): sftp in folder directory
        dir_sftpout (str): sftp out folder directory
    """
    tm1_service.cells.write_values(
        cellset_as_dict={
            ("parameter", "dir_database"): dir_database,
            ("parameter", "dir_log"): dir_log,
            ("parameter", "dir_modelupload"): dir_modelupload,
            ("parameter", "dir_dq"): dir_dq,
            ("parameter", "dir_sftpin"): dir_sftpin,
            ("parameter", "dir_sftpout"): dir_sftpout,
        },
        cube_name="SYS_Parameter",
        dimensions=["03_Parameter", "01_SYS_Parameter"],
    )
