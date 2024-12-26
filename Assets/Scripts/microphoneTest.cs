using UnityEngine;

public class MicrophoneRecord : MonoBehaviour
{
    private AudioClip recordedAudio;

    void Start()
    {
        string[] deviceNames = Microphone.devices;
        if (deviceNames.Length > 0)
        {
            recordedAudio = Microphone.Start(deviceNames[0], true, 10000, 44100);
        }
        else
        {
            Debug.LogError("No microphones found!");
        }
    }

    void Update()
    {
        if (recordedAudio != null && recordedAudio.samples > 0)
        {
            Debug.Log("Recording audio...");
        }
    }
}
