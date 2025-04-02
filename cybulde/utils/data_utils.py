def get_cmd_to_get_raw_data(
    version: str,
    data_local_save_dir: str,
    dvc_remot_repo: str,
    dvc_data_folder: str,
    github_user_name: str,
    github_access_token: str
)->str:
    """Get shell command to download the raw data from dvc store

    Parameters
    ----------
    version: str
        data version
    data_local_save_dir: str
        where to save the downloaded data locally
    dvc_remote_repo: str
        dvc repository that holds information about the data
    dvc_data_folder: str
        location where the remote data is stored
    github_user_name: str
        github user name
    github_access_token: str
        github access token
    
    Returns
    -------
    str
        shell command to download the raw data from dvc store
    """
    without_https = dvc_remote_repo.replace("https://","")
    dvc_remote_repo = f"https://{github_user_name}:{github_access_token}@{without_https}"
    command = "dvc get {dvc_remote_repo} {dvc_raw_data_folder} --rev {version} -o {data_local_save_dir}"
    return command

def get_raw_data_with_version(
    version: str,
    data_local_save_dir: str,
    dvc_remot_repo: str,
    dvc_data_folder: str,
    github_user_name: str,
    github_access_token: str
)->None:
    command = get_cmd_to_get_raw_data(version, data_local_save_dir, dvc_remot_repo, dvc_data_folder, github_user_name, github_access_token)
    subprocess.run(command, shell=True, check=True)