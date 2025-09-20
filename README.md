```mermaid
sequenceDiagram
    participant D as Developer
    participant GP as Git Push
    D->>GP
flowchart LR
    Start --> Input[User Input]
    Input --> Process[Process Data]
    Process --> Valid{Valid?}
    Valid -->|Yes| Save[Save to DB]
    Valid -->|No| Error[Show Error]
    Save --> End
    Error --> Input