function high_energy_indices = best_five_beats(data, best_beat)
    k=1;
    for i=1:2:length(best_beat)
        beat = data(best_beat(i):best_beat(i+1));
        beat_energy(k) = sum(beat.^2); %Finding the energy of all the best beats and storing in an array
        k=k+1;
    end
    sortedEnergy = sort(beat_energy, 'descend'); 
    sortedEnergy = sortedEnergy(1:5); %Taking the top 5 energy beats after storing
    
    k=1;
    for i=1:length(sortedEnergy)
        best_energy(k) = find(beat_energy==sortedEnergy(i)); %Finding the beat corresponding to the energies chosen
        k=k+1;
    end
    
    k=1;
    for j=1:length(best_energy)
        high_energy_indices(k) = best_beat(2*best_energy(j)-1); %Returns the start and stop indices of the 5 chosen beats
        high_energy_indices(k+1) = best_beat(2*best_energy(j));
        k=k+2;
    end
    
end
        