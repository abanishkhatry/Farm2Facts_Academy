# References

Research and resources that inform the pedagogical choices in this program.

## LLM-Assisted Development Education

- **Anthropic (2026). "How AI Assistance Impacts the Formation of Coding Skills."**
  RCT with 52 junior engineers. Students using AI for conceptual inquiry retained skills; those delegating code generation scored 17% lower on comprehension.
  https://www.anthropic.com/research/AI-assistance-coding-skills

- **CodeAid (CHI 2024, Microsoft Research).**
  LLM assistant deployed to 700 students that deliberately avoids giving code solutions. Provides pseudocode, explanations, and fix annotations instead. Four design principles for educational AI.
  https://arxiv.org/abs/2401.11314

- **HypoCompass (IJCAI 2025).**
  Students act as TAs helping an LLM debug code, forcing them to reason about code rather than consume generated solutions.
  https://www.ijcai.org/proceedings/2025/1217.pdf

## Development Practices

- **Osmani, A. (2026). "My LLM Coding Workflow."**
  Practitioner guide for spec-driven, small-chunk LLM-assisted development. "You are the senior dev" principle.
  https://addyosmani.com/blog/ai-coding-workflow/

- **ASDLC.io. "Adversarial Code Review Pattern."**
  Builder/Critic separation with fresh sessions to avoid confirmation bias. Constitutional directive for the Critic role.
  https://asdlc.io/patterns/adversarial-code-review/

- **Fowler, M. "Architecture Decision Records."**
  Lightweight documentation of design decisions. MADR template.
  https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
  https://adr.github.io/

## Testing

- **Meta Engineering (2025). "LLMs Are the Key to Mutation Testing."**
  Using LLMs to generate meaningful mutants and tests to catch them. Validates test quality beyond coverage metrics.
  https://engineering.fb.com/2025/09/30/security/llms-are-the-key-to-mutation-testing-and-better-compliance/

- **LLM4TDD. "Best Practices for Test-Driven Development Using LLMs."**
  Write tests first as specifications, then have LLMs generate implementations that must pass them.
  https://arxiv.org/pdf/2312.04687

## Domain: Food Access

- **Koh, K. et al. (2019). MFAI Methodology.**
  The Monthly Food Access Index methodology that FEAST implements. Defines how household food access scores are calculated based on store proximity, household resources, and trip frequency.

- **USDA Economic Research Service. "Food Access Research Atlas."**
  USDA's definition of food deserts and low-access areas. Background for understanding what FEAST is modeling.
  https://www.ers.usda.gov/data-products/food-access-research-atlas/

## Tools

- **Mesa: Agent-Based Modeling in Python.**
  The ABM framework FEAST uses. Documentation for Model, Agent, GeoSpace, DataCollector.
  https://mesa.readthedocs.io/

- **Claude Code Best Practices.**
  Anthropic's guide for effective use of Claude Code, including context engineering.
  https://docs.anthropic.com/en/docs/claude-code/best-practices
