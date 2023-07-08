%%%%% this code computes the similarity matrix for patch similarity
%%%%% experiment
data_matrix = readtable('cleaned_data.csv');
patch_list = unique(data_matrix.Patch_1_info); % get list of all patches
sim_mat = zeros(length(patch_list),length(patch_list)); % create empty similarity matrix
selected_data = data_matrix(data_matrix.Pass == 1, :); % if first pass: data_matrix.Pass == 1

for i = 1:length(patch_list)
    num_of_pairs = length(patch_list) - i; % number of identity + present-absent unique pairs reduce by 1 as you loop to the next patch in the list
    sim_array = zeros(1,num_of_pairs); 
    for p = 0:num_of_pairs % when p = 0, the first pair would be an identity pair
        % pair index: for any image pair, sometimes image 1 presented
        % first, sometimes image 2 presented first. so we need to create
        % two indexes to look for all the trials with those pairs
        pair_index_1 = selected_data.Patch_1_info == patch_list(i) & selected_data.Patch_2_info == patch_list(i+p);
        pair_index_2 = selected_data.Patch_2_info == patch_list(i) & selected_data.Patch_1_info == patch_list(i+p);
        current_sim_data = selected_data(pair_index_1 | pair_index_2,:);
        sim_array(:,p+1)= median(current_sim_data.similarity);
    end
    sim_mat(i,i:end) = sim_array; % record similarity data in matrix
    sim_mat(i:end,i) = reshape(sim_array,[1,length(sim_array)]);
    
    clear sim_array
    clear current_sim_data
    clear num_of_pairs
    clear pair_index_1
    clear pair_index_2
end

%% make similarity figure
sim_mat_flipped = flip(sim_mat,1); % flip matrix for plotting it in a figure
figure('Color','white');
heatmap(sim_mat_flipped,'CellLabelColor','none');
colour_map = cbrewer2('seq','Greys');
colormap(colour_map); 
title('Patch similarity matrix, second pass');

%% multi-dimensional scaling

[scale_values,e] = cmdscale(sim_mat); % find possible dimensions that explain the similaarity matrix
patch_file_list = unique(data_matrix.Patch_1_name);
patch_file_names = [patch_file_list(15,:); patch_file_list(1:14,:)]; % put present patch to the first of the list

% plot multi-dimensional scaling
figure('Color','white'); % create figure window and axes
axes;
set(gca,'XLim',[-4 4],'YLim',[-4 4]);
ax = gca;
for i = 1:length(patch_file_names)
    current_patch = imread(string(patch_file_names(i,:))); % load current patch in list
    % choose the first two dimensions from the scaling analysis (column 1 and 2)
    x = scale_values(i,1);
    y = scale_values(i,2);
    image(ax,[x-0.35 x+0.35],[y+0.35 y-0.35],current_patch); % plot patch on the figure, based on scaling results
    set(gca,'XLim',[-4 4],'YLim',[-4 4]); % reset the axis limit every loop so it doesn't change everytime a new image is add to the figure
    hold on
    if i == length(patch_file_names) % stop the process once every patch in the list has been run through
        hold off
    end
end
axis square % set figure to square
set(gca, 'YDir','normal','FontSize',12)
xlabel('Dimension 1'),ylabel('Dimension 2')
set(gca,'FontName','Arial','FontSize',12)

%% compare difference between similarity and DxC
all_DxC_data = get_data2(2);
% select DxC data for image 131, location 5
DxC_data = all_DxC_data(all_DxC_data(:,11) == data_matrix.Image_num(1) & all_DxC_data(:,7) == data_matrix.Patch_1_loc(1), :);
% range corrent DxC  from -4,4 to -3.5,3.5
DxC_data(:,9) = DxC_data(:,8).*DxC_data(:,9);
DxC_data(:,9) = DxC_data(:,9) - 0.5;
DxC_data(:,9) = DxC_data(:,8).*DxC_data(:,9);
% get patch info 
patch_info = unique(data_matrix.Patch_1_info);

for i = 2:length(patch_file_names)
    % compute the multisdimensional scaled distance between present patch and each absent patch in
    % the list
    patch_info(i,:)
    x = scale_values(1,1)-scale_values(i,1);
    y = scale_values(1,2)-scale_values(i,2);
    scale_distance(i-1) = sqrt(x^2 + y^2)
    
    % compute the DxC difference between present and each absent patch
    present_DxC = mean(DxC_data(DxC_data(:,12) == 0,9))
    absent_DxC = DxC_data(DxC_data(:,12) == patch_info(i,:),9)
    DxC_difference(i-1) = abs(present_DxC - absent_DxC)   
    
end
[r,p] = corrcoef(scale_distance,DxC_difference);

figure('Color','white');
axes;
set(gca,'XLim',[0 7],'YLim',[0 7]);
ax = gca;
for a = 1:length(scale_distance)
    current_patch = imread(string(patch_file_names(a+1,:))); % load current patch in list
    x = scale_distance(a);
    y = DxC_difference(a);
    image(ax,[x-0.3 x+0.3],[y+0.3 y-0.3],current_patch); 
    set(gca,'XLim',[0 7],'YLim',[0 7]);
    hold on
    if a == length(scale_distance)
        hold off
    end
end
set(gca, 'YDir','normal','FontSize',12)
xlabel('Multidimensional Scale Distance from Present Patch'),ylabel('Absolute DxC Difference from mean Present DxC');
axis square