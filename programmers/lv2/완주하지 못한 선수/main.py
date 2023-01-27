def solution(participant, completion):
    participant_dict = dict()
    answer = ""
    for par in participant:
        participant_dict.setdefault(par, 0)
        participant_dict[par] += 1

    for key in list(participant_dict.keys()):
        if key in completion:
            participant_dict[key] = participant_dict[key] - 1

    for key, value in participant_dict.items():
        if value >= 1:
            answer = key

    return answer


# name = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
name = solution(
    ["mislav", "stanko", "mislav", "ana"],
    ["stanko", "ana", "mislav"]
)

print(name)
