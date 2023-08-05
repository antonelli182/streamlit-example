import streamlit as st
import tempfile

st.title("TITLE LYRIC APP 🎵")

st.header("Upload Your Music")

uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "flac", "aac", "ogg"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    st.audio(tfile.name, format='audio')

    if st.button('Upload'):
        st.write("Uploading...")

        # You can include the code here to handle the upload to your server
        # and process the audio file accordingly.

        progress_bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            progress_bar.progress(i + 1)

        st.success('Upload successful!')
        # You can also use st.error('Upload failed. Please try again.') for error messages.
