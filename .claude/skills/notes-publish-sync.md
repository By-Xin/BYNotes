# Notes Publishing Sync Manager

Intelligent synchronization tool for academic notes following the established publication workflow.

## Purpose

Manages synchronization of academic notes from external sources to the BYNotes publishing system, following the SOP defined in README.md.

## Usage Examples

- "Sync convex optimization notes from external folder to content"
- "Update machine learning notes from ~/Courses/ML to content/MachineLearning" 
- "Sync new topology chapters from source to content/Topology"

## Workflow

### Phase 1: Path Resolution & Setup
- Parse source and target paths from natural language
- Validate paths and create target directories if needed
- Check for existing CATALOG.md or create new one for the topic

### Phase 2: Content Analysis
- Scan source files for markdown content
- Check compliance with README.md markdown standards:
  - Filename conventions (NN_Topic.md format)
  - Required top structure (# Title, References block)
  - Math formatting (KaTeX-safe $$...$$)
  - Proper heading hierarchy
- Calculate file hashes and modification times

### Phase 3: Change Detection & Reporting  
- Compare with existing target content and catalog
- Identify new files, modifications, and potential issues
- Generate comprehensive sync report:
  - Files to be added/updated
  - Format compliance issues found
  - Version differences from catalog

### Phase 4: Confirmation & Execution
- Present detailed sync plan for user approval
- Execute approved operations:
  - Copy/update files to target directory
  - Apply format corrections if needed
  - Update or create CATALOG.md with new versions
- Follow README.md publish workflow:
  - Run format checks
  - Prepare for local preview
  - Stage for git commit

## Standards Compliance

Ensures all synced content follows:
- Filename conventions (A-Z a-z 0-9 _ - ( ) only)
- Required markdown structure
- Math notation standards (KaTeX compatibility)  
- Reference block format
- Heading hierarchy rules

## Version Tracking

- Maintains CATALOG.md for each topic directory
- Tracks SHA256 hashes and modification times
- Preserves sync status notes and warnings
- Integrates with git workflow for change management