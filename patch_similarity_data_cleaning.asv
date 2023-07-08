%%%%%% this code cleans the data for patch similarity experiment

% load raw data file names
folder1 = 'C:\Users\aufb\Desktop\intern\data'; 
filePattern1 = fullfile(folder1,'*.csv');
allFiles1 = struct2cell(dir(filePattern1));
data_file = string(allFiles1(1,:)); % here, we load all data file names into one row array

% Initialize date_matrix
data_matrix = [];
% loop through every data file
a = 0;
for i = 1:size(data_file,2)
    % load current data file
    current_file = readtable(data_file(:,i));
    
    % first, go through every data file to check whether it is complete; if
    % they are incomplete, skip them - has to contain trial number
    % (experiment begun) and max trial number must be 240 (experiment was completed)
    if sum(strcmp('trialNumber',current_file.Properties.VariableNames)) == 0 || max(current_file.trialNumber) < 240
        continue
    end
    
    % then, select only the useful data columns and rows: descriptives, trial
    % number, image num, location 1, location 2, patch 1 info, patch 2 info, 
    % patch 1 name, patch 2 name, pass, similarity, response time
 
    current_selected_data = current_file(:,{'participant','OS','frameRate','trialNumber','Pair_type','Pass','Image_num','Patch_1_loc','Patch_2_loc','Patch_1_info','Patch_2_info',...
        'Patch_1_name','Patch_2_name','similarity','response_time'});
    current_selected_data(isnan(current_selected_data.trialNumber),:) = []; % remove data that contains nan
    
    % add subject number
    a = a+1;
    current_selected_data = addvars(current_selected_data,a.*ones(size(current_selected_data,1),1), 'Before','participant','NewVariableNames',"Subject_number"); 
    
    
    % add to big matrix
    if i == 1
        data_matrix = current_selected_data;
    else
        data_matrix = vertcat(data_matrix, current_selected_data);
    end
    
    clear current_file
    clear current_selected_data
end

%% check first and second pass similarity distribution 
% data_matrix = readtable("200_Participants_data.csv");
data_matrix = readtable('cleaned_data.csv');
figure('Color','white');
histogram(data_matrix.similarity(data_matrix.Pass == 1),'FaceAlpha',0.5);
hold on
histogram(data_matrix.similarity(data_matrix.Pass == 2),'FaceAlpha',0.5);
hold off
legend({'First pass','Second pass'});
xlabel('Similarity rating'),ylabel('Count');

%% verify double-pass correlation per-participant

subject_num = unique(data_matrix.Subject_number);
subject_id = unique(data_matrix.participant);
sub_pass_corr = [];

for s = 1:length(subject_num)
    current_subject = data_matrix(data_matrix.Subject_number == s, :); % select current subject data
    a = 1;
    for p = 1:max(data_matrix.trialNumber)/2
        % first pass pair
        current_pair_first = current_subject(p,:);
        % second pass pair
        current_pair_second = current_subject(current_subject.Patch_1_info == current_pair_first.Patch_1_info & current_subject.Patch_2_info == current_pair_first.Patch_2_info & ...
            current_subject.Pass == 2,:);
        subject_pass_similarity(a,:) = [current_pair_first.similarity current_pair_second.similarity]; % record similiarity of first and second pass
        
        a = a+1;
        
        clear current_pair_first
        clear current_pair_second
    end
     if s == 1 || s == 92 || s == 112
        disp(s)
        figure;
        histogram(subject_pass_similarity(:,1), 'FaceAlpha',0.5);
        hold  on
        histogram(subject_pass_similarity(:,2), 'FaceAlpha',0.5);
        hold off
        [r,p] = corrcoef(subject_pass_similarity(:,1),subject_pass_similarity(:,2))
     end
[r,p] = corrcoef(subject_pass_similarity(:,1),subject_pass_similarity(:,2)); % compute overall double-pass correlation  
sub_pass_corr(s,:) = [s r(1,2) p(1,2)]; % record correlation for subject

clear current_subject
clear subject_pass_similarity
end
% plot correlation
figure('Color','white');
histogram(sub_pass_corr(:,2))
title('Double pass correlations of participants'), xlabel('Pearson Correlation (r)'), ylabel('Count');

%% 
% set the threshold for minimum acceptable correlation = 0.4
threshold = 0.4; 
low_corr_participants = find(sub_pass_corr(:, 2) < threshold);
% record original size
original_size = size(data_matrix, 1);

% Get the subject numbers of the low correlation participants
low_corr_subject_numbers = subject_num(low_corr_participants);

% Remove participants with low double-pass correlation from the data matrix
data_matrix = data_matrix(~ismember(data_matrix.Subject_number, low_corr_subject_numbers), :);

% Print eliminated subject numbers
eliminated_subjects = setdiff(subject_num, data_matrix.Subject_number);
disp('Eliminated subject numbers:');
disp(eliminated_subjects);


%% 
%check which rows got removed
updated_size = size(data_matrix, 1);
eliminated_rows = original_size - updated_size;

if eliminated_rows > 0
    eliminated_subject_numbers = unique(data_matrix(original_size - eliminated_rows + 1:end, 'Subject_number'));
    disp('Eliminated rows:');
    disp(eliminated_subject_numbers);
else
    disp('No rows eliminated.');
end

%% now that we have verified the validity of data, we can save the data matrix to a csv file

writetable(data_matrix,'cleaned_data.csv');

% writetable(data_matrix,'online_pilot_data_25.csv');

%dfd
