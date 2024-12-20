�
    ��Rg�  �                   ��   � d dl mZmZmZ d dlmZ d dlmZ d dlmZ d dlm	Z	mZ  G d� de�  �        Z
 G d� dee�  �        Zd dlmZ d dlmZ d dlm	Z	mZ  G d	� d
ej        �  �        ZdS )�    )�AbstractBaseUser�BaseUserManager�PermissionsMixin)�models)�settings)�	timedelta�datetimec                   �   � e Zd Zdd�Zdd�ZdS )�CustomUserManagerNc                 ��   � |st          d�  �        �| �                    |�  �        } | j        dd|i|��}|�                    |�  �         |�                    | j        ��  �         |S )NzThe Email field must be set�email)�using� )�
ValueError�normalize_email�model�set_password�save�_db)�selfr   �password�extra_fields�users        �kC:\Users\tushar sharma\Desktop\WEBDEV\Dotanalytics\integrated_project\DOTANALYTICS\authentication\models.py�create_userzCustomUserManager.create_user   sw   � �� 	<��:�;�;�;��$�$�U�+�+���t�z�6�6��6��6�6�����(�#�#�#��	�	���	�!�!�!���    c                 �  � |�                     dd�  �         |�                     dd�  �         |�                    d�  �        durt          d�  �        �|�                    d�  �        durt          d�  �        � | j        ||fi |��S )N�is_staffT�is_superuserz"Superuser must have is_staff=True.z&Superuser must have is_superuser=True.)�
setdefault�getr   r   )r   r   r   r   s       r   �create_superuserz"CustomUserManager.create_superuser   s�   � ����
�D�1�1�1������5�5�5����J�'�'�t�3�3��A�B�B�B����N�+�+�4�7�7��E�F�F�F��t���x�@�@�<�@�@�@r   �N)�__name__�
__module__�__qualname__r   r"   r   r   r   r   r      sB   � � � � � �� � � �
A� 
A� 
A� 
A� 
A� 
Ar   r   c                   �   � e Zd Z ej        d��  �        Z ej        dd��  �        Z ej        dd��  �        Z ej	        d��  �        Z
 ej	        d��  �        Z ej        d��  �        Z e�   �         ZdZg Zd	� Zd
S )�
CustomUserT)�unique�   )�
max_length�blank)�defaultF��auto_now_addr   c                 �   � | j         S r#   )r   �r   s    r   �__str__zCustomUser.__str__,   s
   � ��z�r   N)r$   r%   r&   r   �
EmailFieldr   �	CharField�
first_name�	last_name�BooleanField�	is_activer   �DateTimeField�date_joinedr   �objects�USERNAME_FIELD�REQUIRED_FIELDSr2   r   r   r   r(   r(      s�   � � � � � ��F��T�*�*�*�E�!��!�R�t�<�<�<�J� �� �B�d�;�;�;�I�#��#�D�1�1�1�I�"�v�"�5�1�1�1�H�&�&�&�D�9�9�9�K���!�!�G��N��O�� � � � r   r(   c                   �   � e Zd Z ej        ej        ej        ��  �        Z ej	        d��  �        Z
 ej        d��  �        Zd� ZdS )�PasswordResetOTP)�	on_delete�   )r+   Tr.   c                 �\   � t          j        �   �         | j        z
  t          d��  �        k     S )z:Check if the OTP is still valid (e.g., within 10 minutes).�
   )�minutes)r	   �now�
created_atr   r1   s    r   �is_otp_validzPasswordResetOTP.is_otp_valid:   s%   � ��|�~�~���/�)�B�2G�2G�2G�G�Gr   N)r$   r%   r&   r   �
ForeignKeyr   �AUTH_USER_MODEL�CASCADEr   r4   �otpr9   rF   rG   r   r   r   r?   r?   5   sn   � � � � � ��6��X�5���P�P�P�D�
�&�
�a�
(�
(�
(�C�%��%�4�8�8�8�J�H� H� H� H� Hr   r?   N)�django.contrib.auth.modelsr   r   r   �	django.dbr   �django.confr   r	   r   r   r(   �Modelr?   r   r   r   �<module>rP      sO  �� Z� Z� Z� Z� Z� Z� Z� Z� Z� Z� � � � � � �  �  �  �  �  �  � � � � � � � (� (� (� (� (� (� (� (�A� A� A� A� A�� A� A� A�.� � � � �!�#3� � � �& !�  �  �  �  �  � � � � � � � (� (� (� (� (� (� (� (�H� H� H� H� H�v�|� H� H� H� H� Hr   