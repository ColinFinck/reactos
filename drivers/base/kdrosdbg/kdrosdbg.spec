@ stdcall KdD0Transition()
@ stdcall KdD3Transition()
@ stdcall KdDebuggerInitialize0(ptr)
@ stdcall KdDebuggerInitialize1(ptr)
@ stdcall KdReceivePacket(long ptr ptr ptr ptr)
@ stdcall KdRestore(long)
@ stdcall KdSave(long)
@ stdcall KdSendPacket(long ptr ptr ptr)

; Legacy KD
@ stdcall KdPortGetByteEx(ptr ptr)
@ stdcall KdPortInitializeEx(ptr long long)
@ stdcall KdPortPutByteEx(ptr long)
