�
    ��Rgy  �                   �   � d dl mZ d dlmZ d dlmZ d dlmZ ddlm	Z	  e�   �         Z
 G d� dej        �  �        Z G d	� d
ej        �  �        ZdS )�    )�get_user_model)�serializers)�validate_password)�UniqueValidator�   )�
CustomUserc                   ��   � e Zd Z ej        d eej        �                    �   �         ��  �        g��  �        Z	 ej
        ddeg��  �        Z ej
        dd��  �        Z G d� d�  �        Zd� Zd	� Zd
� ZdS )�RegisterSerializerT)�queryset)�required�
validators)�
write_onlyr   r   �r   r   c                   �   � e Zd ZeZdZdS )�RegisterSerializer.Meta)�email�password�	password2N)�__name__�
__module__�__qualname__�User�model�fields� �    �nC:\Users\tushar sharma\Desktop\WEBDEV\Dotanalytics\integrated_project\DOTANALYTICS\authentication\serilizer.py�Metar      s   � � � � � ���4���r   r   c                 �   � t           j        �                    |��  �        �                    �   �         rt	          j        d�  �        �|S )z7
        Check if the email is already in use.
        )r   z&A user with this email already exists.)r   �objects�filter�existsr   �ValidationError)�self�values     r   �validate_emailz!RegisterSerializer.validate_email   sD   � � ��$�$�5�$�1�1�8�8�:�:� 	X��-�.V�W�W�W��r   c                 �V   � |d         |d         k    rt          j        ddi�  �        �|S )Nr   r   zPassword fields didn't match.)r   r#   )r$   �attrss     r   �validatezRegisterSerializer.validate"   s3   � �����k� 2�2�2��-�z�;Z�.[�\�\�\��r   c                 �`   � t           j        �                    |d         |d         ��  �        }|S )Nr   r   )r   r   )r   r    �create_user)r$   �validated_data�users      r   �createzRegisterSerializer.create(   s5   � ��|�'�'� ��)�#�J�/� (� 
� 
��
 �r   N)r   r   r   r   �
EmailFieldr   r   r    �allr   �	CharFieldr   r   r   r   r&   r)   r.   r   r   r   r
   r
   	   s�   � � � � � �"�K�"��#�O�T�\�-=�-=�-?�-?�@�@�@�A�� � �E� %�{�$���%�&�� � �H�
 &��%���E�E�E�I�5� 5� 5� 5� 5� 5� 5� 5�
� � �� � �� � � � r   r
   c                   �T   � e Zd Z ej        d��  �        Z ej        dd��  �        ZdS )�LoginSerializerT)r   r   N)r   r   r   r   r/   r   r1   r   r   r   r   r3   r3   0   s:   � � � � � �"�K�"�D�1�1�1�E�$�{�$��t�D�D�D�H�H�Hr   r3   N)�django.contrib.authr   �rest_frameworkr   �'django.contrib.auth.password_validationr   �rest_framework.validatorsr   �modelsr   r   �ModelSerializerr
   �
Serializerr3   r   r   r   �<module>r;      s�   �� .� .� .� .� .� .� &� &� &� &� &� &� E� E� E� E� E� E� 5� 5� 5� 5� 5� 5� � � � � � ��~����%� %� %� %� %��4� %� %� %�NE� E� E� E� E�k�,� E� E� E� E� Er   