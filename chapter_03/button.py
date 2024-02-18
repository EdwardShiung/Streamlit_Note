import streamlit as st
import time

st.title('Buttons and Sliders')

## Buttons
st.header('Button')
# st.button

# Create a Button
button = st.button('button')

if button:
    st.write("You have clicked the Button")
else:
    st.write("You have not clicked the Button")

st.code('''

# Create a Button
button = st.button('button')

if button:
    st.write("You have clicked the Button")
else:
    st.write("You have not clicked the Button")

''')

## Radio Buttons
st.header('Radio')
# st.radio

#Create a Radio
radio = st.radio

gender = st.radio(
    "Select Your Gender",
    ('Male', 'Female', 'Others')
)

if(gender == 'Male'):
    st.write('You have selected Male.')
elif (gender == 'Female'):
    st.write('You have selected Female.')
elif (gender == 'Others'):
    st.write('You have selected others.')

st.write('The first option is selected by default')

st.code('''

radio = st.radio

gender = st.radio(
    "Select Your Gender",
    ('Male', 'Female', 'Others')
)

if(gender == 'Male'):
    st.write('You have selected Male.')
elif (gender == 'Female'):
    st.write('You have selected Female.')
elif (gender == 'Others'):
    st.write('You have selected others.')

''')

## Check Boxes
st.header("Check Box")
# st.checkbox

st.write('Please Select Your Hobies:')
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.write('The check box created can be preselected.')
check_4 = st.checkbox("Accept All Terms and Conditions", value=True)

st.code('''

st.write('Please Select Your Hobies:')
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.write('The check box created can be preselected.')
check_4 = st.checkbox("Accept All Terms and Conditions", value=True)


'''
)

## Drop-Downs (Select Box)
st.header('Select Box')
# st.selectbox

st.write("Creating Dropbox for hobby")
hobby = st.selectbox(
    'Choose your hobby:',
    ('Books', 'Movies','Sports')
)
st.write('The first option is selected by default.')

st.write('We still can change the default option by index:')
candidate = st.selectbox(
    'Choose Your Candidate:',
    ('Michael', 'Edward', 'Daniel'),
    index = 1
)

st.code('''
st.write("Creating Dropbox for hobby")
hobby = st.selectbox(
    'Choose your hobby:',
    ('Books', 'Movies','Sports')
)
st.write('The first option is selected by default.')

st.write('We still can change the default option by index:')
candidate = st.selectbox(
    'Choose Your Candidate:',
    ('Michael', 'Edward', 'Daniel'),
    index = 1
)

''')

## Multiselects
st.header('Multiselects')
# st.multiselect

st.write("Let's select your hobbie:")
hobbies_1 = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/ TV Series', 'Playing']
)

st.write('We still can set the default:')
hobbies_2 = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/ TV Series', 'Playing'],
    ['Cooking']
)

st.code('''

st.write("Let's select your hobbie:")
hobbies_1 = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/ TV Series', 'Playing']
)

st.write('We still can set the default:')
hobbies_2 = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/ TV Series', 'Playing'],
    ['Cooking']
)

''')

## Download Button
st.header("Download Button")
# st.download_button

# Creating Download Button
# down_btn = st.download_button(
#     label="Download Image",
#     data=open("./fam.jpg", "rb"),
#     file_name="lions.jpg",
#     mime="image/jpg"
# )

down_btn = st.download_button(
    label="Download CSV",
    data=open("./files/avocado.csv", "rb"),
    file_name="data.csv",
    mime="csv"
)

st.code('''

down_btn = st.download_button(
    label="Download CSV",
    data=open("./files/avocado.csv", "rb"),
    file_name="data.csv",
    mime="csv"
)

''')

## Progress Bars
st.header("Progress Bar")
st.progress


# Define Progress Bar
st.header("Progress Bar")
download = st.progress(0)

for percentage in range(100):
    time.sleep(0.0000001)
    download.progress(percentage + 1)
st.write('Download Complete')

st.code('''

# Define Progress Bar
st.header("Progress Bar")
download = st.progress(0)

for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)
st.write('Download Complete')

''')


## Spinners
st.header("Spinner")
# st.spinner
with st.spinner('Loading...'):
    time.sleep(5)
    st.write('hello Data Scientists')