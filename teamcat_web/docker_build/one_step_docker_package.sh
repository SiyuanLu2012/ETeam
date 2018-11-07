rm -rf ./target/one_step_build
mkdir -p ./target/one_step_build
cp -r ./one_step_build ./target
cp -r ../doraemon/ ./target/one_step_build/teamcat
cd ..
cd teamcat_font_end
npm run build
cd ../docker_build
cp -r ../teamcat_font_end/dist ./target/one_step_build/nginx
cp -r ./target/one_step_build/teamcat/doraemon/static ./target/one_step_build/nginx
cp -f ./target/one_step_build/teamcat/settings.py ./target/one_step_build/teamcat/doraemon/
