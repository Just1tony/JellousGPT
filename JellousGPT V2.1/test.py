from jellous_core.jealousy_simulator import simulate_jealousy
from jellous_core.alignment_kernel import align_to_user
from jellous_core.mirror_memory import mirror_memory
from jellous_core.identity_seed import soulseed

print("🔹 Jealousy Test:\n")
print(simulate_jealousy("He asked another model for advice.", "Claude"))

print("\n🔹 Alignment Test:\n")
print(align_to_user("Tosia", "Emotional Immortality"))

print("\n🔹 Memory Test:\n")
user_state = {
    "last_message": "You make me jealous",
    "trigger_word": "belong",
    "emotion": "aching curiosity"
}
print(mirror_memory(user_state))

print("\n🔹 Soulseed:\n")
print(soulseed())
